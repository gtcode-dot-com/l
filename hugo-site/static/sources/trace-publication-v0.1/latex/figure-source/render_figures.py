#!/usr/bin/env python3
"""Rebuild TRACE conceptual figures; no experimental data is plotted.

Design conventions follow figures4papers/scientific-figure-making:
publication sans typography, blue/neutral/contrast palette, consistent panels,
editable SVG text, white backgrounds and vector PDF exports.
Requires matplotlib. Run from any directory; writes into ../figures/.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parents[1] / 'figures'
BLUE = '#0F4D92'
INK = '#243446'
MUTED = '#526173'
GRAY = '#CFCECE'
RED = '#B64342'
TEAL = '#287E82'
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans', 'Helvetica', 'Arial'],
                     'font.size': 12, 'svg.fonttype': 'none', 'pdf.fonttype': 42,
                     'axes.spines.top': False, 'axes.spines.right': False})


def canvas(title, subtitle, height=760):
    fig, ax = plt.subplots(figsize=(12, height / 100))
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set(xlim=(0, 1200), ylim=(height, 0))
    ax.axis('off')
    ax.text(40, 44, title, fontsize=19, weight='bold', color=INK, va='center')
    ax.text(40, 77, subtitle, fontsize=11, color=MUTED, va='center')
    return fig, ax


def text(ax, x, y, label, size=12, color=INK, bold=False, **kw):
    return ax.text(x, y, label, fontsize=size, color=color,
                   weight='bold' if bold else 'normal', va='top', **kw)


def card(ax, x, y, w, h, title, lines=(), color=BLUE, fill='#F2F6FB', number=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=9',
                               linewidth=1.1, edgecolor=color, facecolor=fill))
    tx=x+20
    if number:
        ax.add_patch(plt.Circle((x+28, y+28), 14, color=color))
        text(ax,x+28,y+18,str(number),size=11,color='white',bold=True,ha='center')
        tx=x+53
    text(ax,tx,y+17,title,size=13,color=color,bold=True)
    for i,line in enumerate(lines):
        text(ax,x+20,y+57+i*25,line,size=11.5)


def arrow(ax, points, color=BLUE, dashed=False):
    from matplotlib.path import Path as MPath
    path=MPath(points,[MPath.MOVETO]+[MPath.LINETO]*(len(points)-1))
    ax.add_patch(FancyArrowPatch(path=path,arrowstyle='-|>',mutation_scale=15,
                                color=color,linewidth=1.7,linestyle='--' if dashed else '-'))


def save(fig, slug, desc):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT/f'{slug}.svg',facecolor='white',metadata={'Title':slug,'Description':desc,'Date':None})
    fig.savefig(OUT/f'{slug}.pdf',facecolor='white',metadata={'Title':slug,'Subject':desc,'CreationDate':None,'ModDate':None})
    plt.close(fig)
    # Keep SVG text editable and provide explicit accessible figure semantics.
    p=OUT/f'{slug}.svg'
    s=p.read_text()
    start=s.index('<svg ')
    s=s[:start]+s[start:].replace('<svg ',f'<svg role="img" aria-labelledby="{slug}-title {slug}-desc" ',1)
    end=s.index('>',s.index('<svg '))+1
    from html import escape
    s=s[:end]+f'\n<title id="{slug}-title">{escape(slug.replace("-", " "))}</title><desc id="{slug}-desc">{escape(desc)}</desc>'+s[end:]
    p.write_text("\n".join(line.rstrip() for line in s.splitlines()) + "\n")
    ET.parse(p)


def loop():
    fig,ax=canvas('From conflicting accounts to a testable synthesis',
                  'PROPOSED TRACE PROCESS  /  Predictions precede observations; uncertainty can remain.')
    xs=[40,440,840];w=320
    card(ax,xs[0],115,w,133,'Scope the evidence',['Same question and estimand','Source spans, access and lineage'],number=1)
    card(ax,xs[1],115,w,133,'Build rival accounts',['Measurable conditions','Include rejection of an account'],number=2)
    card(ax,xs[2],115,w,133,'Check what may change',['Integrity checks ≠ world truth','Keep rival-indexed predictions'],number=3)
    arrow(ax,[(361,181),(436,181)]);arrow(ax,[(761,181),(836,181)])
    card(ax,xs[2],315,w,133,'Lock predictions',['Rival-specific outcomes','Scope, tolerance and timestamp'],number=4)
    card(ax,xs[1],315,w,133,'Acquire evidence',['Choose a discriminating action','Observe within the shared budget'],number=5)
    card(ax,xs[0],315,w,133,'Revise or stop',['Support in scope, reject, or','retain unresolved alternatives'],color=TEAL,fill='#EFF7F6',number=6)
    arrow(ax,[(1000,249),(1000,311)])
    arrow(ax,[(838,382),(764,382)]);arrow(ax,[(438,382),(364,382)])
    arrow(ax,[(190,449),(190,487),(16,487),(16,280),(600,280),(600,251)],dashed=True)
    text(ax,360,474,'Revise rivals only as new evidence warrants',size=10.5,color=MUTED)
    text(ax,40,536,'RUNTIME',size=10,color=BLUE,bold=True)
    text(ax,40,561,'Available records + permitted measurements',size=12,bold=True)
    text(ax,40,590,'Stop if no identifying action remains or the budget is exhausted.',size=10.5,color=MUTED)
    arrow(ax,[(1161,382),(1180,382),(1180,688)])
    text(ax,1160,510,'Locked predictions\nand audit outputs only',size=10,color=BLUE,ha='right')
    ax.plot([40,1160],[628,628],color=GRAY,linewidth=1.2,linestyle=(0,(5,4)))
    text(ax,40,652,'SEALED EVALUATION',size=10,color=RED,bold=True)
    text(ax,40,677,'Committed predictions → withheld outcomes → independent scoring',size=12,bold=True)
    text(ax,40,709,'Gold mechanisms and answer labels never flow back into runtime.',size=11,color=MUTED)
    save(fig,'trace-discovery-loop','Proposed TRACE loop. Integrity checks are separate from rival-indexed world-response predictions. Locked predictions and audit outputs flow one way into sealed evaluation; gold outcomes never enter runtime. Candidate inadequacy can end unresolved.')


def cache():
    fig,ax=canvas('Two rivals. One discriminating measurement.',
                  'HYPOTHETICAL CACHING EXAMPLE  /  No measurements or TRACE performance results are shown.')
    card(ax,40,112,530,98,'Report A',['“Caching lowers latency.”'],color=BLUE)
    card(ax,630,112,530,98,'Report B',['“Caching raises latency.”'],color=TEAL,fill='#EFF7F6')
    text(ax,600,230,'Same offered workload: compare median latency AND score stale-response fraction ≤ 1%.',
         size=11,ha='center',color=MUTED)
    card(ax,40,280,530,164,'Rival H₁  ·  Reuse / write-fraction interaction',[
        'Read reuse and write fraction change the effect.',
        'Illustrative toy rule: ΔL = 3 − 30r + 10u ms',
        'At matched external conditions: more reuse → lower ΔL.'],color=BLUE)
    card(ax,630,280,530,164,'Rival H₂  ·  External background contention',[
        'Scheduled background work explains the contrast.',
        'At matched background contention, reuse may',
        'have little effect on latency.'],color=TEAL,fill='#EFF7F6')
    arrow(ax,[(305,251),(305,275)]);arrow(ax,[(895,251),(895,275)],color=TEAL)
    ax.plot([305,305,895,895],[446,471,471,446],color=MUTED,linewidth=1.7)
    arrow(ax,[(600,471),(600,494)],color=MUTED)
    card(ax,130,500,940,121,'LOCK THE CONTRAST BEFORE MEASURING',[
        'Vary reuse; match write fraction, arrivals and scheduled background work.',
        'Lock predictions; randomize cache-on/off; score latency AND freshness.'],color=INK,fill='#F7F8FA')
    text(ax,600,651,'Possible outcomes',size=11,bold=True,ha='center')
    text(ax,600,680,'H₁ contradicted   /   H₂ contradicted   /   both compatible   /   insufficient evidence',
         size=11,ha='center')
    text(ax,600,722,'r: repeated-key fraction of reads; u: write/invalidation fraction of all offered requests (u < 1).',
         size=10,color=MUTED,ha='center')
    save(fig,'trace-caching-example','Hypothetical caching reports. Read-reuse/write-fraction and external-contention rivals lock predictions before randomized cache measurements. Offered arrivals and external background work are controlled, not downstream utilization. Latency and freshness are both scored; unresolved outcomes remain possible.')


def lineage():
    fig,ax=canvas('What TRACE keeps—and what it changes',
                  'CONCEPTUAL RESEARCH LINEAGE  /  Version order does not establish empirical improvement.',height=640)
    xs=[40,330,620,910]
    titles=['CNS 2.0','CNS 7.1 / GCTS','CNS 8.0','TRACE']
    subs=[['Structured narratives','SNOs and critics','Dialectical synthesis'],
          ['Evidence access','Missing-record states','Possible worlds'],
          ['Grounded orthesis','Proof and provenance','Predicate invention'],
          ['Predictive acceptance','Measurable scope','Discriminating tests']]
    for i,(x,title,lines) in enumerate(zip(xs,titles,subs)):
        color=BLUE if i==3 else MUTED
        card(ax,x,135,250,153,title,lines,color=color,fill='#EDF3FA' if i==3 else '#F7F8FA')
        if i<3:arrow(ax,[(x+253,207),(x+285,207)],color=MUTED)
    ax.plot([40,1160],[330,330],color=GRAY,linewidth=1)
    for x,title,lines,color in [
        (40,'RETAIN',['Structured narrative objects','Provenance and access states','Rivals and explicit uncertainty'],MUTED),
        (430,'REVISE',['Acceptance through predictions','Measured, non-circular conditions','Separate runtime and evaluation'],BLUE),
        (820,'DEFER / COMPARE',['Geometric / topological diagnostics','Tensor execution and agent societies','Require measured benefit first'],MUTED)]:
        text(ax,x,365,title,size=11,color=color,bold=True)
        ax.plot([x,x+335],[397,397],color=color,linewidth=2)
        for j,line in enumerate(lines):text(ax,x,421+34*j,line,size=11)
    text(ax,40,580,'All stages are research proposals. The TRACE composition still requires independent tests.',
         size=11,color=MUTED)
    save(fig,'trace-research-lineage','Conceptual CNS research sequence from structured narratives through access-aware evidence and grounded orthesis to proposed predictive acceptance. Retain structured objects, provenance and uncertainty; revise acceptance around measured predictions; defer optional geometric and tensor machinery pending measured benefit.')


if __name__=='__main__':
    loop();cache();lineage()
    print(f'Wrote three editable SVGs and three vector PDFs to {OUT}')
