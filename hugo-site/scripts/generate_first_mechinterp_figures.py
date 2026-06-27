from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content" / "articles" / "first-mechanistic-interpretability-attempt-self-ground"


plt.rcParams.update(
    {
        "svg.fonttype": "none",
        "font.family": "DejaVu Sans",
        "axes.titlesize": 17,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
    }
)


PALETTE = {
    "ink": "#17202a",
    "muted": "#5d6976",
    "grid": "#d8dee6",
    "blue": "#2f6fbb",
    "teal": "#1f9d8a",
    "red": "#c94c4c",
    "orange": "#d88728",
    "green": "#3b8f5a",
    "purple": "#7a5dbb",
    "bg": "#f7f9fb",
    "line": "#2b3a4a",
}


def save(fig: plt.Figure, filename: str, *, tight: bool = True) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    save_kwargs = {"format": "svg", "facecolor": "white"}
    if tight:
        save_kwargs["bbox_inches"] = "tight"
    fig.savefig(OUT / filename, **save_kwargs)
    plt.close(fig)


def draw_research_arc() -> None:
    fig, ax = plt.subplots(figsize=(13.5, 6.5))
    fig.subplots_adjust(left=0.055, right=0.955, top=0.79, bottom=0.12)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    fig.text(
        0.5,
        0.925,
        "SELF-GROUND became useful when the evidence got stricter",
        ha="center",
        fontsize=18,
        weight="bold",
        color=PALETTE["ink"],
    )
    fig.text(
        0.5,
        0.872,
        "The arc moved from real-path validation, to decoded SAE intervention, to specificity failure, to smaller causal practice loops.",
        ha="center",
        fontsize=11.5,
        color=PALETTE["muted"],
    )

    y = 55
    ax.plot([10, 90], [y, y], color=PALETTE["line"], lw=2.2, solid_capstyle="round")
    xs = [13, 28, 42, 56, 71, 86]
    colors = [
        PALETTE["blue"],
        PALETTE["teal"],
        PALETTE["orange"],
        PALETTE["red"],
        PALETTE["purple"],
        PALETTE["green"],
    ]
    labels = [
        ("Phase 1/2", "Real activations,\nSAE compatibility,\ndecoded patch path"),
        ("E002", "Serious GPU run:\nreal movement,\ncontrol > target"),
        ("E003", "Task calibration fixed;\nspecificity worsened"),
        ("E004", "15-cell rescue matrix;\nbest aggregate positive,\nno candidate cells"),
        ("MechLedger", "Audit kernel extracted\nfrom the overclaiming\nproblem"),
        ("Local MI Lab", "GPT-2 small practice:\ncontrols, hook_z,\nreplication"),
    ]
    dates = [
        "Jun 20",
        "Jun 21",
        "Jun 21",
        "Jun 24",
        "Jun 25",
        "Jun 26",
    ]

    for i, (x, color, (title, body), date) in enumerate(zip(xs, colors, labels, dates)):
        ax.scatter([x], [y], s=280, color=color, zorder=4, edgecolor="white", linewidth=2)
        ax.text(x, y - 9.5, date, ha="center", va="top", fontsize=10, color=PALETTE["muted"])
        top = y + 10 if i % 2 == 0 else y - 38
        box = FancyBboxPatch(
            (x - 10.75, top),
            21.5,
            22,
            boxstyle="round,pad=0.65,rounding_size=2.2",
            fc="#ffffff",
            ec=color,
            lw=1.6,
        )
        ax.add_patch(box)
        ax.text(x, top + 16, title, ha="center", va="center", fontsize=11, color=color, weight="bold")
        ax.text(x, top + 8.5, body, ha="center", va="center", fontsize=8.6, color=PALETTE["ink"], linespacing=1.15)
        if i % 2 == 0:
            ax.plot([x, x], [y + 2.5, top], color=color, lw=1.3)
        else:
            ax.plot([x, x], [y - 2.5, top + 22], color=color, lw=1.3)

    ax.text(
        50,
        8,
        "The repeated pattern: make the claim narrower, add a control, then let the artifact say no when it says no.",
        ha="center",
        va="center",
        fontsize=12,
        color=PALETTE["ink"],
        weight="bold",
    )

    save(fig, "research-arc.svg", tight=False)


def draw_specificity_results() -> None:
    runs = ["E002\nuncalibrated", "E003\ncalibrated", "E004 best\naggregate"]
    target = np.array([0.0341995, 0.6277370, 0.8960492])
    control = np.array([0.0546811, 0.7188387, 0.7598730])
    gaps = target - control

    fig, ax = plt.subplots(figsize=(10.8, 6.3))
    x = np.arange(len(runs))
    width = 0.32
    ax.bar(x - width / 2, target, width, label="Target prompt movement", color=PALETTE["blue"])
    ax.bar(x + width / 2, control, width, label="Matched/control movement", color=PALETTE["red"])
    ax.axhline(0, color=PALETTE["ink"], lw=1)
    ax.set_ylim(-0.18, 1.08)
    ax.set_ylabel("Mean absolute logit-contrast delta")
    ax.set_xticks(x)
    ax.set_xticklabels(runs)
    ax.set_title("The intervention moved logits before it earned a mechanism claim")
    ax.grid(axis="y", color=PALETTE["grid"], lw=0.9)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, loc="upper left")

    for idx, (t, c, gap) in enumerate(zip(target, control, gaps)):
        ax.text(idx - width / 2, t + 0.025, f"{t:.3f}", ha="center", va="bottom", fontsize=9, color=PALETTE["ink"])
        ax.text(idx + width / 2, c + 0.025, f"{c:.3f}", ha="center", va="bottom", fontsize=9, color=PALETTE["ink"])
        color = PALETTE["green"] if gap > 0 else PALETTE["red"]
        y = max(t, c) + 0.105
        ax.text(idx, y, f"gap {gap:+.3f}", ha="center", va="center", color=color, fontsize=10, weight="bold")

    ax.text(
        2,
        0.18,
        "E004 improved the aggregate gap,\nbut multi-control min gap = -0.019\nand family min gap = -0.090.",
        ha="center",
        va="center",
        fontsize=9.5,
        color=PALETTE["orange"],
        bbox=dict(boxstyle="round,pad=0.45", fc="#fff8ed", ec=PALETTE["orange"], lw=1.1),
    )
    fig.text(
        0.09,
        0.02,
        "Data from SELF-GROUND run ledger and claim ledger. All three runs remained insufficient_evidence/no candidate evidence.",
        fontsize=9,
        color=PALETTE["muted"],
    )

    save(fig, "specificity-results.svg")


def draw_causal_filter() -> None:
    fig, ax = plt.subplots(figsize=(10.8, 8.6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    fig.text(
        0.055,
        0.945,
        "The induction practice loop filtered attractive false positives",
        fontsize=18,
        weight="bold",
        color=PALETTE["ink"],
    )
    fig.text(
        0.055,
        0.907,
        "Each gate made the result less flashy and more defensible.",
        fontsize=11.5,
        color=PALETTE["muted"],
    )

    steps = [
        (
            "Behavior",
            "GPT-2 small predicted repeated tokens.\nPositive prompts looked clean.",
            "64/64 rank <= 10",
            PALETTE["blue"],
        ),
        (
            "Attention",
            "Previous-occurrence attention surfaced\nL0H1, L0H5, L0H10, L11H8.",
            "descriptive only",
            PALETTE["teal"],
        ),
        (
            "Controls",
            "Distractor and wrong-token controls\nalso scored strongly.",
            "false positives exposed",
            PALETTE["orange"],
        ),
        (
            "Layer patch",
            "Layer-level attn_out patching moved\nsome candidates, but not head-specifically.",
            "seed-1 downgraded",
            PALETTE["red"],
        ),
        (
            "Head hook",
            "hook_z exposed a real head axis;\npatch scope became single_head_z.",
            "head_specific_patch=true",
            PALETTE["purple"],
        ),
        (
            "Replication",
            "Five narrow heads replicated by rule,\nwith L7H7 strongest but still local.",
            "not an induction claim",
            PALETTE["green"],
        ),
    ]

    x = 7
    w = 86
    h = 10.2
    ys = [78, 66, 54, 42, 30, 18]
    for i, (y, (title, body, tag, color)) in enumerate(zip(ys, steps)):
        box = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.55,rounding_size=2.2",
            fc="#ffffff",
            ec=color,
            lw=1.6,
        )
        ax.add_patch(box)
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                2.0,
                h,
                boxstyle="round,pad=0.55,rounding_size=2.2",
                fc=color,
                ec=color,
                lw=0,
            )
        )
        ax.text(x + 7.2, y + h / 2, title, ha="left", va="center", fontsize=12, color=color, weight="bold")
        ax.text(x + 25, y + h / 2, body, ha="left", va="center", fontsize=9.2, color=PALETTE["ink"], linespacing=1.12)
        ax.text(
            x + w - 13,
            y + h / 2,
            tag,
            ha="center",
            va="center",
            fontsize=8.5,
            color="white",
            bbox=dict(boxstyle="round,pad=0.28", fc=color, ec=color),
        )
        if i < len(steps) - 1:
            arrow = FancyArrowPatch(
                (50, y - 0.5),
                (50, ys[i + 1] + h + 0.5),
                arrowstyle="-|>",
                mutation_scale=14,
                lw=1.4,
                color=PALETTE["line"],
            )
            ax.add_patch(arrow)

    ax.text(
        50,
        6.5,
        "The practice loop produced a stricter experimental reflex: each attractive interpretation had to survive a concrete control.",
        ha="center",
        va="center",
        fontsize=11.5,
        color=PALETTE["ink"],
        weight="bold",
    )

    save(fig, "causal-filter.svg")


def main() -> None:
    draw_research_arc()
    draw_specificity_results()
    draw_causal_filter()


if __name__ == "__main__":
    main()
