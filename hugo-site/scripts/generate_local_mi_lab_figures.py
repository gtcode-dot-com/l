from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content" / "articles" / "local-mi-lab-gpt2-small-induction-controls"

plt.rcParams.update(
    {
        "svg.fonttype": "none",
        "font.family": "DejaVu Sans",
        "axes.titlesize": 16,
        "axes.labelsize": 10.5,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
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
    "gray": "#73808c",
    "line": "#2b3a4a",
}


def save(fig: plt.Figure, filename: str, *, tight: bool = True) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    kwargs = {"format": "svg", "facecolor": "white"}
    if tight:
        kwargs["bbox_inches"] = "tight"
    fig.savefig(OUT / filename, **kwargs)
    plt.close(fig)


def add_box(
    ax: plt.Axes,
    x: float,
    y: float,
    w: float,
    h: float,
    color: str,
    title: str,
    body: str,
) -> None:
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.7,rounding_size=2.5",
        fc="#ffffff",
        ec=color,
        lw=1.7,
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h - 6, title, ha="center", va="center", fontsize=11.5, weight="bold", color=color)
    ax.text(x + w / 2, y + h / 2 - 4, body, ha="center", va="center", fontsize=8.6, color=PALETTE["ink"], linespacing=1.15)


def draw_practice_loop() -> None:
    fig, ax = plt.subplots(figsize=(13.5, 6.2))
    fig.subplots_adjust(left=0.055, right=0.955, top=0.78, bottom=0.12)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    fig.text(
        0.5,
        0.925,
        "Local MI Lab got useful when every attractive result faced a stricter test",
        ha="center",
        fontsize=18,
        weight="bold",
        color=PALETTE["ink"],
    )
    fig.text(
        0.5,
        0.872,
        "The work moved from descriptive attention to causal patching, held-out prompts, and fixed-candidate characterization.",
        ha="center",
        fontsize=11.5,
        color=PALETTE["muted"],
    )

    y = 53
    ax.plot([9, 91], [y, y], color=PALETTE["line"], lw=2.2, solid_capstyle="round")
    xs = [9, 25.4, 41.8, 58.2, 74.6, 91]
    colors = [PALETTE["blue"], PALETTE["teal"], PALETTE["orange"], PALETTE["purple"], PALETTE["gray"], PALETTE["red"]]
    labels = [
        ("Baseline", "64/64 positives\nranked target\ninside top 10"),
        ("Controls", "Raw previous-token\nattention also fired\non control families"),
        ("Layer Patching", "attn_out moved\ncontrols; random heads\nlooked better"),
        ("hook_z Sweep", "72 heads x 3 seeds;\nfive narrow\nlocal candidates"),
        ("Held-Out", "16 fixed heads;\n11 falsified,\n5 downgraded"),
        ("Characterization", "All 16 fixed heads\nclassified as\nfalsified_candidate"),
    ]

    for i, (x, color, (title, body)) in enumerate(zip(xs, colors, labels)):
        ax.scatter([x], [y], s=270, color=color, zorder=4, edgecolor="white", linewidth=2)
        top = y + 10 if i % 2 == 0 else y - 38
        add_box(ax, x - 8.1, top, 16.2, 22, color, title, body)
        if i % 2 == 0:
            ax.plot([x, x], [y + 2.5, top], color=color, lw=1.3)
        else:
            ax.plot([x, x], [y - 2.5, top + 22], color=color, lw=1.3)

    ax.text(
        50,
        8,
        "Each step narrowed the claim, then gave controls and characterization another chance to break it.",
        ha="center",
        va="center",
        fontsize=12,
        color=PALETTE["ink"],
        weight="bold",
    )

    save(fig, "local-mi-lab-loop.svg", tight=False)


def draw_candidate_gaps() -> None:
    heads = ["L7H7", "L9H11", "L7H11", "L7H0", "L0H8"]
    multiseed = np.array([0.080596, 0.035749, 0.025868, 0.010526, 0.007738])
    heldout = np.array([-0.009352, -0.049409, 0.182858, 0.074392, 0.000563])
    characterized = np.array([-0.0550, -0.0048, -0.1316, -0.0336, -0.1949])

    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    x = np.arange(len(heads))
    width = 0.24
    ax.bar(x - width, multiseed, width, label="Original multi-seed gap", color=PALETTE["blue"])
    ax.bar(x, heldout, width, label="Held-out mean gap", color=PALETTE["orange"])
    ax.bar(x + width, characterized, width, label="Characterization mean gap", color=PALETTE["red"])
    ax.axhline(0, color=PALETTE["ink"], lw=1)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{head}\nfalsified" for head in heads])
    ax.set_ylabel("Mean positive-minus-control gap")
    ax.set_title("Characterization closed the candidate set")
    ax.grid(axis="y", color=PALETTE["grid"], lw=0.9)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right")
    ax.margins(x=0.04)

    note = "All five primary heads ended as falsified_candidate after attention/effect, position, OV/QK, and prompt-family checks."
    fig.text(0.5, 0.02, note, ha="center", fontsize=10.5, color=PALETTE["muted"])
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    save(fig, "candidate-heldout-gaps.svg")


def draw_heldout_status() -> None:
    groups = ["Prior\nreplicated", "Prior raw\nattention", "Negative\ncontrols", "All fixed\nheads"]
    downgraded = np.array([2, 2, 1, 5])
    falsified = np.array([3, 3, 5, 11])

    fig, ax = plt.subplots(figsize=(10.8, 6.0))
    x = np.arange(len(groups))
    ax.bar(x, downgraded, color=PALETTE["orange"], label="downgraded")
    ax.bar(x, falsified, bottom=downgraded, color=PALETTE["red"], label="falsified")
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.set_ylabel("Candidate count")
    ax.set_ylim(0, 18)
    ax.set_title("Held-out robustness downgraded or falsified every fixed head")
    ax.grid(axis="y", color=PALETTE["grid"], lw=0.9)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper left")

    totals = downgraded + falsified
    for i, total in enumerate(totals):
        ax.text(i, total + 0.35, f"{total}", ha="center", va="bottom", fontsize=10, color=PALETTE["ink"], weight="bold")

    fig.text(
        0.5,
        0.02,
        "Seed-level survival rows still appeared, including on negative controls; the consolidated rule downgraded or falsified every fixed head.",
        ha="center",
        fontsize=10.3,
        color=PALETTE["muted"],
    )
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    save(fig, "heldout-status.svg")


def draw_characterization_status() -> None:
    groups = ["Primary\nheads", "Prior raw\nattention", "Negative\ncontrols", "All fixed\nheads"]
    falsified = np.array([5, 5, 6, 16])
    total = np.array([5, 5, 6, 16])

    fig, ax = plt.subplots(figsize=(10.8, 6.0))
    x = np.arange(len(groups))
    ax.bar(x, falsified, color=PALETTE["red"], label="falsified_candidate")
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.set_ylabel("Candidate count")
    ax.set_ylim(0, 18)
    ax.set_title("Characterization falsified every fixed head")
    ax.grid(axis="y", color=PALETTE["grid"], lw=0.9)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper left")

    for i, (falsified_count, total_count) in enumerate(zip(falsified, total)):
        ax.text(
            i,
            falsified_count + 0.35,
            f"{falsified_count}/{total_count}",
            ha="center",
            va="bottom",
            fontsize=10,
            color=PALETTE["ink"],
            weight="bold",
        )

    fig.text(
        0.5,
        0.02,
        "The fixed set included five primary heads, five prior raw-attention heads, and six negative controls; none strengthened.",
        ha="center",
        fontsize=10.3,
        color=PALETTE["muted"],
    )
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    save(fig, "characterization-status.svg")


def draw_failure_taxonomy() -> None:
    modes = [
        "control_moved",
        "target_swap_leak",
        "domain_flip",
        "length_flip",
        "intervention_disagreement",
        "reversed_control_leak",
        "position_mismatch",
    ]
    counts = np.array([80, 54, 40, 40, 40, 26, 16])
    labels = [
        "Controls\nmoved",
        "Target-swap\nleak",
        "Domain\nflip",
        "Length\nflip",
        "Intervention\ndisagreement",
        "Reversed-control\nleak",
        "Position\nmismatch",
    ]
    colors = [
        PALETTE["red"],
        PALETTE["orange"],
        PALETTE["blue"],
        PALETTE["teal"],
        PALETTE["purple"],
        PALETTE["gray"],
        PALETTE["green"],
    ]

    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    x = np.arange(len(modes))
    ax.bar(x, counts, color=colors)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Row-level failure labels")
    ax.set_ylim(0, 90)
    ax.set_title("The taxonomy made the candidate failures specific")
    ax.grid(axis="y", color=PALETTE["grid"], lw=0.9)
    ax.set_axisbelow(True)

    for i, value in enumerate(counts):
        ax.text(i, value + 2, str(value), ha="center", va="bottom", fontsize=10, color=PALETTE["ink"], weight="bold")

    fig.text(
        0.5,
        0.02,
        "Across the primary counterexample artifacts, the failure labels concentrated on controls moving, target-swap leakage, and domain/length instability.",
        ha="center",
        fontsize=10.3,
        color=PALETTE["muted"],
    )
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    save(fig, "failure-taxonomy.svg")


def draw_metric_calibration() -> None:
    families = [
        "clean format\nvariant",
        "clean\nnumber",
        "clean\nsymbolic",
        "clean\nword",
        "frequency trap\ncontrol",
        "no-repeat\ncontrol",
        "reversed-order\ncontrol",
        "same-frequency\ncontrol",
        "target-swap\ncontrol",
        "wrong-target\nsame prompt",
    ]
    values = np.array(
        [
            6.2758,
            4.7463,
            5.2454,
            1.7428,
            3.2170,
            0.0835,
            -1.0967,
            -0.2299,
            -3.5317,
            -3.9115,
        ]
    )
    is_positive = np.array([True, True, True, True, False, False, False, False, False, False])
    colors = [PALETTE["blue"] if flag else PALETTE["gray"] for flag in is_positive]
    colors[4] = PALETTE["red"]

    fig, ax = plt.subplots(figsize=(12.2, 6.2))
    x = np.arange(len(families))
    ax.bar(x, values, color=colors)
    ax.axhline(0, color=PALETTE["ink"], lw=1)
    ax.axhline(1.7428, color=PALETTE["orange"], lw=1.2, linestyle="--", label="Weakest positive mean")
    ax.set_xticks(x)
    ax.set_xticklabels(families)
    ax.set_ylabel("Mean true-vs-control logit diff")
    ax.set_title("Metric calibration stopped the next candidate search")
    ax.grid(axis="y", color=PALETTE["grid"], lw=0.9)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right")

    for i, value in enumerate(values):
        offset = 0.18 if value >= 0 else -0.28
        va = "bottom" if value >= 0 else "top"
        ax.text(i, value + offset, f"{value:.2f}", ha="center", va=va, fontsize=8.8, color=PALETTE["ink"])

    fig.text(
        0.5,
        0.02,
        "The frequency-trap control averaged 3.2170 with fraction_diff_positive = 1.0, above the weakest positive family mean of 1.7428.",
        ha="center",
        fontsize=10.3,
        color=PALETTE["muted"],
    )
    fig.tight_layout(rect=(0, 0.075, 1, 1))
    save(fig, "metric-calibration.svg")


def main() -> None:
    draw_practice_loop()
    draw_candidate_gaps()
    draw_heldout_status()
    draw_characterization_status()
    draw_failure_taxonomy()
    draw_metric_calibration()


if __name__ == "__main__":
    main()
