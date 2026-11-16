#!/usr/bin/env python3
"""Render the shared Markdown manuscript into TeX and (optionally) Hugo text.

Requires Pandoc. With no arguments rebuilds main.tex only. --hugo updates the
paper in an existing checkout, keeping its front matter. --check checks parity
without writing. PDF compilation remains a separate offline build.sh step.
"""
from pathlib import Path
import argparse,html,json,re,subprocess,tempfile
HERE=Path(__file__).resolve().parent
FIGURES=[
 ('cns-9-discovery-loop','Proposed discovery loop. Integrity checks and rival-indexed predictions precede acquisition. Only committed outputs cross into sealed evaluation; no gold outcomes return to runtime.'),
 ('cns-9-caching-example','Hypothetical caching contrast. Reuse/write-fraction and external-contention rivals commit predictions before a separating measurement. Downstream utilization is not held fixed; latency and freshness are both scored.'),
 ('cns-9-research-lineage','Conceptual research lineage, not measured improvement. CNS 9.0 retains structured evidence and uncertainty while evaluating predictive acceptance against simpler alternatives.')]

def latex_fragment(s):
 return subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash+citations+raw_tex','--to=latex','--natbib','--shift-heading-level-by=-1','--no-highlight'],input=s,text=True,capture_output=True,check=True).stdout

def tex_source(master):
 prepared=re.sub(r'^(#{2,3})\s+\d+(?:\.\d+)*\.?\s+',r'\1 ',master,flags=re.M)
 abstract,body=prepared.removeprefix('## Abstract\n\n').split('\n## ',1)
 for i,(slug,caption) in enumerate(FIGURES,1):
  latex='\n'.join([r'\begin{figure}[htbp]',r'\centering',rf'\includegraphics[width=\linewidth]{{figures/{slug}.pdf}}',rf'\caption{{{caption}}}',rf'\label{{fig:{slug}}}',r'\end{figure}'])
  body=body.replace('{{FIGURE_'+str(i)+'}}',latex)
 text=latex_fragment('## '+body)
 text=text.replace(r'\begin{verbatim}',r'\par\medskip'+'\n'+r'\noindent\begin{minipage}{\linewidth}'+'\n'+r'\begin{CNSAlgorithm}').replace(r'\end{verbatim}',r'\end{CNSAlgorithm}'+'\n'+r'\end{minipage}\par\medskip')
 text=re.sub(r'\\texttt\{([^{}]+)\}',lambda m:r'\CNSIdentifier{'+m[1]+'}',text)
 text=re.sub(r'(?=\\section\{Proposed operational\s+algorithm\})',lambda _:r'\Needspace{12\baselineskip}'+ '\n',text)
 return (HERE/'template.tex').read_text().replace('%%ABSTRACT%%',latex_fragment(abstract).strip()).replace('%%BODY%%',text.strip())

def web_body(master,records):
 refs={r['id']:r for r in records};order=[]
 def cite(m):
  ids=re.findall(r'@([A-Za-z0-9]+)',m[0]);links=[]
  for rid in ids:
   assert rid in refs,rid
   if rid not in order:order.append(rid)
   links.append(f'[{order.index(rid)+1}](#ref-{rid})')
  return '['+', '.join(links)+']'
 out=re.sub(r'\[@[^\]]+\]',cite,master)
 for i,(slug,caption) in enumerate(FIGURES,1):
  figure=f'<figure>\n  <img src="/papers/cns-9/figures/{slug}.svg" alt="{html.escape(caption,quote=True)}" loading="lazy" decoding="async" style="max-width:100%;height:auto;">\n  <figcaption>Figure {i}. {caption}</figcaption>\n</figure>'
  out=out.replace('{{FIGURE_'+str(i)+'}}',figure)
 out+='\n## References\n\n'
 for n,rid in enumerate(order,1):
  r=refs[rid]
  out+=f'<a id="ref-{rid}"></a>**[{n}] {r["authors"]} ({r["year"]}). {r["title"]}.**<br>\n{r["url"]}\n\n'
 out+='''## Publication downloads and self-citation

- [Compiled research PDF](/papers/cns-9/cns-9-research-proposal.pdf) · [Standalone LaTeX source](/papers/cns-9/cns-9-latex-source.zip) · [BibTeX self-citation](/papers/cns-9/cns-9-citation.bib)
- [Annotated reference registry](/papers/cns-9/references.json) · [Bibliography](/papers/cns-9/references.bib) · [Proposed protocol YAML](/papers/cns-9/proposed-evaluation-protocol.yaml)

**How to cite:** GTCode.com. (2026, November 15). *Chiral Narrative Synthesis 9.0: Falsification-Guided Narrative Synthesis for Predictive Knowledge Discovery* (Research proposal, version 0.1). https://gtcode.com/papers/cns-9/
'''
 return out,len(order)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--hugo',action='store_true');ap.add_argument('--check',action='store_true');args=ap.parse_args()
 master=(HERE/'manuscript.md').read_text();tex=tex_source(master)
 if args.check:assert (HERE/'main.tex').read_text()==tex,'main.tex differs from master/template'
 else:(HERE/'main.tex').write_text(tex)
 if args.hugo:
  root=next(p for p in HERE.parents if p.name=='hugo-site')
  page=root/'content/papers/cns-9/index.md';original=page.read_text();front=original.split('---',2)[1]
  records=json.loads((root/'static/papers/cns-9/references.json').read_text())
  body,count=web_body(master,records)
  lead='''\n> **Research proposal · Version 0.1 · 15 November 2026.** CNS 9.0 has not yet been empirically evaluated. This paper is neither peer reviewed nor preregistered.

[Read the accessible overview](/guides/cns-9/overview/) · [See the proposed evaluation protocol](/guides/cns-9/evaluation/) · [Download PDF](/papers/cns-9/cns-9-research-proposal.pdf) · [Download LaTeX source](/papers/cns-9/cns-9-latex-source.zip)

'''
  rendered='---'+front+'---\n'+lead+body
  if args.check:assert original==rendered,'Hugo article differs from master'
  else:page.write_text(rendered)
  print(f'Hugo and TeX share one manuscript; {count} cited sources.')
