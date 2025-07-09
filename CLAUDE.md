# CLAUDE.md - Development Guidelines

## Build/Deployment Commands
- Site is static HTML/CSS/JS - no build process required
- Deploy by pushing changes to the repository

## Testing
- Test responsive layouts at 1440px, 1024px, 768px, and 480px breakpoints
- Check mermaid chart rendering on all device sizes
- Verify ocean animation performance on mobile devices
- Test touch interactions on iOS and Android

## Code Style Guidelines

### HTML
- Use semantic HTML5 elements
- Maintain proper indentation (4 spaces)
- Include appropriate accessibility attributes

### CSS
- Follow mobile-first responsive design principles
- Use CSS variables for theme colors and values
- Organize styles by component
- Media queries: 1024px (tablets), 768px (mobile), 480px (small mobile)

### JavaScript
- Optimize for performance on mobile devices
- Prefer ES6+ syntax
- Check device capabilities before using WebGL/3D features
- Use async/defer for script loading

### Performance
- Optimize images and assets
- Implement lazy loading for below-fold content
- Reduce complexity for mobile animations
- Ensure smooth scrolling and transitions

### Security
- No external dependencies apart from approved CDNs
- Sanitize any user inputs
- Follow content security best practices