#!/usr/bin/env python3
import os, re
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter

HERE = os.path.dirname(__file__)
CORPUS = os.path.join(HERE, '..', 'data', 'care_endurance_corpus.csv')
LEX = os.path.join(HERE, '..', 'data', 'theme_lexicon.csv')
OUT = os.path.join(HERE, '..', 'output')
os.makedirs(OUT, exist_ok=True)

df = pd.read_csv(CORPUS)
lex = pd.read_csv(LEX)

def tokenize(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    return [w for w in t.split() if w]

df["tokens"] = df["text"].apply(tokenize)
df["token_count"] = df["tokens"].apply(len)
df["type_token_ratio"] = df["tokens"].apply(lambda toks: len(set(toks))/max(1,len(toks)))

# naive sentiment lexicon (demo)
POS = {"gentle","kindness","heal","mercy","compassion","light","lantern"}
NEG = {"ruin","burden","collapse"}
def sent(toks):
    p = sum(1 for w in toks if w in POS)
    n = sum(1 for w in toks if w in NEG)
    return (p-n)/max(1,len(toks))
df["sentiment"] = df["tokens"].apply(sent)

# Author column (short label)
df["author_short"] = df["author"].str.split().str[0]

# --- Docs per author
ax = df["author_short"].value_counts().sort_index().plot(kind="bar", title="Documents per Author")
ax.set_xlabel("Author"); ax.set_ylabel("Count")
fig = ax.get_figure(); fig.tight_layout()
fig.savefig(os.path.join(OUT, "docs_per_author.png")); plt.close(fig)

# --- Average metrics per author
for col in ["token_count","type_token_ratio","sentiment"]:
    agg = df.groupby("author_short")[col].mean()
    ax = agg.plot(kind="bar", title=f"Average {col} by Author")
    ax.set_xlabel("Author"); ax.set_ylabel(col)
    fig = ax.get_figure(); fig.tight_layout()
    fig.savefig(os.path.join(OUT, f"avg_{col}_by_author.png")); plt.close(fig)

# --- Theme hits by author using lexicon
kw_to_theme = dict(zip(lex["keyword"], lex["theme"]))
def theme_counts(tokens):
    c = Counter()
    for w in tokens:
        if w in kw_to_theme:
            c[kw_to_theme[w]] += 1
    return c

df["theme_counts"] = df["tokens"].apply(theme_counts)
theme_df = []
for _, row in df.iterrows():
    for th in ["care","endurance"]:
        theme_df.append({"author_short": row["author_short"], "theme": th, "hits": row["theme_counts"].get(th,0)})
theme_df = pd.DataFrame(theme_df)
agg_theme = theme_df.groupby(["author_short","theme"])["hits"].sum().unstack(fill_value=0)

ax = agg_theme.plot(kind="bar", title="Theme Hits by Author")
ax.set_xlabel("Author"); ax.set_ylabel("Hits")
fig = ax.get_figure(); fig.tight_layout()
fig.savefig(os.path.join(OUT, "theme_hits_by_author.png")); plt.close(fig)

# --- Top keywords per author (stopworded)
STOP = {"the","and","a","an","of","to","in","is","it","that","this","as","on","for","by","with","from","into","not","has","have","had","was","were"}
def top_words(texts):
    c = Counter()
    for toks in texts:
        c.update([w for w in toks if w not in STOP and len(w)>2 and not w.isdigit()])
    return c.most_common(15)

for author in df["author_short"].unique():
    items = top_words(df[df["author_short"]==author]["tokens"].tolist())
    if items:
        words, counts = zip(*items)
        fig = plt.figure()
        plt.bar(range(len(words)), counts)
        plt.xticks(range(len(words)), words, rotation=45, ha="right")
        plt.title(f"Top Keywords — {author}")
        plt.tight_layout()
        fig.savefig(os.path.join(OUT, f"top_keywords_{author}.png"))
        plt.close(fig)

# --- Co-occurrence network (author-agnostic, window = doc)
G = nx.Graph()
for toks in df["tokens"]:
    uniq = list(sorted(set([w for w in toks if w not in STOP and len(w)>2])))
    for i in range(len(uniq)):
        for j in range(i+1,len(uniq)):
            a,b = uniq[i], uniq[j]
            if G.has_edge(a,b):
                G[a][b]["weight"] += 1
            else:
                G.add_edge(a,b, weight=1)

pos = nx.spring_layout(G, seed=11)
plt.figure()
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, width=[G[u][v]["weight"] for u,v in G.edges()])
nx.draw_networkx_labels(G, pos, font_size=7)
plt.axis("off"); plt.tight_layout()
plt.savefig(os.path.join(OUT, "cooccurrence_network.png")); plt.close()

# export summary
summary = df[["id","author","year","theme_hint","token_count","type_token_ratio","sentiment"]]
summary.to_csv(os.path.join(OUT, "summary_metrics.csv"), index=False)
print("Analysis complete. Outputs written to output/.")
