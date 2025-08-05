# Methodology & Style Guide

## Writing Style Guide (Goal 1: Content Quality Enhancement)

### Filler Language to Eliminate
- Meta-commentary: "this is a research roadmap", "this chapter aims to", "to this end"
- Hedge words: "so-called", "it is important to note that", "we believe that"
- Redundant explanations: "as mentioned previously", "as we will see", "it should be noted"
- Weak transitions: "moving on to", "next we will look at", "another thing to consider"

### Language Elevation Patterns
- Replace "We will look at..." → "This experiment investigates..."
- Replace "This is hard because..." → "Key challenges include..."
- Replace "The goal is to..." → "This research validates..."
- Replace "It would be good to..." → "The methodology requires..."

### List-to-Narrative Conversion Rule
Lists should only be used for:
- Sequential experimental steps
- Distinct technical components
- Enumerated requirements

Convert to narrative when items represent:
- Related concepts that flow together
- Explanatory content
- Background information

## Statistical Validation Template (Goal 2: Mathematical Rigor)

### Standard Experimental Validation Protocol Template

```markdown
#### Experimental Validation Protocol: [Experiment Name]

**1. Hypothesis:**
- *Null Hypothesis (H₀):* [State the null hypothesis]
- *Alternative Hypothesis (H₁):* [State the alternative hypothesis]

**2. Method:**
- The single manual example serves as the prototype for DSPy-driven automated generation
- This prototype enables production of statistically significant sample sizes

**3. Sample Size Calculation:**
- To detect a medium effect size (d = 0.5) with statistical power of 0.8 at significance level (α) of 0.05
- Required sample size calculated using two-sample t-test formula:
  `n = ((Z_α/2 + Z_β)² × (σ₁² + σ₂²)) / (μ₁ - μ₂)²`
- Power analysis indicates requirement of **n ≈ 64** samples per group for robust validation

**4. Success Criteria:**
- Reject null hypothesis with **p-value < 0.05**
- Observe Cohen's d effect size **d > 0.5**
- Demonstrate statistical significance across validation metrics
```

### Mathematical Notation Standards
- Use standard statistical symbols (α, β, σ, μ)
- Present formulas in simple, recognizable format
- Include concrete sample size numbers
- Specify effect sizes and confidence intervals

## Implementation Integration Protocol (Goal 3: Research-Development Alignment)

### Mapping Requirements
Every experimental phase must:
- Cite specific modules from `building-cns-2.0-developers-guide`
- Reference corresponding implementation chapters
- Specify technical prerequisites from developer guide
- Connect validation approaches to system capabilities

### Integration Template
```markdown
*Implementation Note: This validation leverages the [specific component] described in Chapter [X] of the developer's guide, requiring [technical prerequisites] and enabling [validation capabilities].*
```

### Resource Estimation Framework
- Timeline estimates based on implementation complexity
- Technical prerequisite identification from developer guide
- Validation protocol specifications using DSPy capabilities
- Feasibility constraints grounded in system architecture

## Content Refinement Process

### Phase 1: Filler Elimination
1. Identify and remove meta-commentary
2. Eliminate redundant explanatory text
3. Replace weak language with precise technical terms
4. Convert appropriate lists to narrative prose

### Phase 2: Statistical Integration
1. Insert Experimental Validation Protocol template
2. Add mathematical formulations for sample sizes
3. Specify concrete statistical success criteria
4. Connect manual examples to automated generation

### Phase 3: Implementation Alignment
1. Add developer guide cross-references
2. Specify technical prerequisites
3. Establish realistic resource requirements
4. Connect research to system capabilities

### Quality Validation Checklist
- [ ] Filler content reduced to <10%
- [ ] Technical language at PhD level
- [ ] Statistical frameworks mathematically sound
- [ ] Implementation mappings accurate and feasible
- [ ] Document structure preserved while improving substance