# Building CNS 2.0: A Developer's Guide - Project Overview

## Overview

This is an educational blog project built with Hugo that provides a comprehensive developer's guide to implementing Chiral Narrative Synthesis (CNS) 2.0 in Python. The project serves as a progressive learning resource that bridges theoretical concepts from an academic research paper with practical, production-ready code implementations.

The blog takes readers through a six-chapter journey, from understanding the core concepts of CNS 2.0 to building a complete, research-grade implementation. Each chapter includes detailed Python code examples, mathematical formula implementations, and clear explanations that connect theory to practice through "From Paper to Code" sections.

**Recent Update (July 30, 2025)**: Implemented hybrid static/Hugo architecture where the homepage, investigation pages, and agent pages serve as pure static HTML files, while the CNS educational guide maintains Hugo processing for dynamic content generation. Added comprehensive development guide (DEV_GUIDE.md) for local building and GitHub Pages deployment.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
The project uses **Hugo**, a static site generator, with the following key components:

1. **Template System**: Custom Hugo layouts in `layouts/_default/` for consistent page structure
2. **Content Management**: Markdown-based content in `content/guides/building-cns-2.0-developers-guide/`
3. **Styling**: Custom CSS with mobile-first responsive design in `static/css/style.css`
4. **Math Rendering**: KaTeX library for displaying mathematical formulas
5. **Syntax Highlighting**: Prism.js for code block styling with line numbers
6. **Icons**: Feather Icons for UI elements

### Backend Architecture
Since this is a static site generator project, there's no traditional backend. However, the content structure follows these patterns:

1. **Chapter-Based Organization**: Six sequential chapters with progressive complexity
2. **Weight-Based Ordering**: Hugo's weight system for proper chapter sequencing
3. **Cross-Chapter Navigation**: Previous/Next navigation between chapters
4. **Table of Contents**: Auto-generated TOC for each chapter

### Content Structure
```
content/
├── guides/
│   └── building-cns-2.0-developers-guide/
│       ├── _index.md (Guide overview)
│       ├── chapter-1-introduction.md
│       ├── chapter-2-sno-foundations.md
│       ├── chapter-3-critic-pipeline.md
│       ├── chapter-4-synthesis-engine.md
│       ├── chapter-5-system-integration.md
│       └── chapter-6-complete-implementation.md
```

## Key Components

### 1. Hugo Configuration
- **Static Site Generation**: Hugo processes Markdown content into HTML
- **Template System**: Baseof template with individual page layouts
- **Math Rendering**: KaTeX integration for displaying mathematical formulas
- **Code Highlighting**: Prism.js for syntax highlighting with line numbers

### 2. Educational Content Structure
- **Progressive Learning**: Six chapters building from basic concepts to complete implementation
- **Theory-to-Code Mapping**: Explicit connections between research paper formulas and Python code
- **Interactive Elements**: Code examples, mathematical formulas, and visual diagrams

### 3. Python Implementation Examples
The content includes complete Python implementations of:
- Structured Narrative Objects (SNOs)
- Multi-Component Critic Pipeline
- Generative Synthesis Engine
- System Integration and Workflow Management

### 4. Responsive Design
- **Mobile-First CSS**: Responsive breakpoints for tablets and phones
- **Clean Typography**: Inter font family with proper spacing and readability
- **Dark Theme Code Blocks**: Professional syntax highlighting with line numbers

## Data Flow

### Content Creation Flow
1. **Markdown Authoring**: Content written in Markdown with Hugo front matter
2. **Hugo Processing**: Static site generator processes content and templates
3. **Asset Optimization**: CSS/JS minification and optimization
4. **Static Output**: Generated HTML/CSS/JS files in `public/` directory

### User Experience Flow
1. **Landing Page**: Guide overview with chapter navigation
2. **Sequential Reading**: Progressive chapter-by-chapter learning
3. **Cross-References**: Links between related concepts across chapters
4. **Code Examples**: Syntax-highlighted Python implementations
5. **Mathematical Formulas**: KaTeX-rendered equations and definitions

## External Dependencies

### Frontend Libraries
- **KaTeX**: Math rendering library for displaying LaTeX formulas
- **Prism.js**: Syntax highlighting for code blocks
- **Feather Icons**: Icon set for UI elements
- **Google Fonts**: Inter and JetBrains Mono font families

### Build Tools
- **Hugo**: Static site generator (Go-based)
- **CSS**: Custom responsive styles with CSS Grid and Flexbox
- **JavaScript**: Minimal vanilla JS for navigation and interactions

### Python Libraries (Referenced in Content)
The educational content covers implementations using:
- **transformers**: Hugging Face library for language models
- **torch**: PyTorch for neural network operations
- **faiss-cpu**: Facebook AI Similarity Search for approximate nearest neighbors
- **numpy**: Numerical computing
- **dataclasses**: Python data structure definitions

## Deployment Strategy

### Static Site Deployment
1. **Build Process**: Hugo generates static files in `public/` directory
2. **Asset Management**: CSS, JS, and image files served from `static/` directory
3. **CDN Delivery**: Static files can be deployed to any CDN or static hosting service

### Development Workflow
1. **Local Development**: Hugo server with live reload for content editing
2. **Content Updates**: Markdown file modifications automatically rebuild site
3. **Version Control**: Git-based workflow for content and code changes

### Production Considerations
- **SEO Optimization**: Proper meta tags, structured data, and semantic HTML
- **Performance**: Minified CSS/JS, optimized images, and efficient loading
- **Accessibility**: Semantic markup, proper heading hierarchy, and keyboard navigation
- **Mobile Experience**: Responsive design with touch-friendly navigation

The project represents a modern educational platform that effectively bridges complex theoretical concepts with practical implementation, making advanced AI research accessible to developers through clear, progressive instruction.