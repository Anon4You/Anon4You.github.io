---
name: Alienkrishn Portfolio
description: Terminal-inspired developer portfolio for open-source enthusiasts
colors:
  bg: "#111411"
  surface: "#191d18"
  text: "#eff2e9"
  muted: "#a5afa0"
  accent: "#c2f970"
  line: "#30382c"
typography:
  display:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    letterSpacing: "-2px"
  heading:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    letterSpacing: "-1px"
  body:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontWeight: 400
  mono:
    fontFamily: "ui-monospace, SFMono-Regular, Consolas, monospace"
rounded:
  sm: "5px"
  md: "8px"
  lg: "9px"
  xl: "12px"
spacing:
  xs: "8px"
  sm: "16px"
  md: "22px"
  lg: "26px"
  xl: "30px"
  xxl: "40px"
  xxxl: "56px"
  xxxxl: "60px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#19200f"
    rounded: "{rounded.sm}"
    padding: "13px 21px"
    fontWeight: 600
    fontSize: "14px"
    transition: "background .2s, transform .2s"
  button-primary-hover:
    backgroundColor: "#d5ff9b"
    transform: "translateY(-2px)"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "13px 21px"
    fontWeight: 600
    fontSize: "14px"
  button-secondary-hover:
    color: "{colors.accent}"
  skip-link:
    backgroundColor: "{colors.accent}"
    color: "{colors.bg}"
    position: "fixed"
    top: "12px"
    left: "12px"
    padding: "10px 20px"
    borderRadius: "{rounded.sm}"
    transform: "translateY(-180%)"
    zIndex: 10
  skip-link-focus:
    transform: "translateY(0)"
  terminal:
    backgroundColor: "#171c16"
    border: "1px solid #3b4633"
    borderRadius: "{rounded.xl}"
    transform: "rotate(2deg)"
    boxShadow: "20px 24px 80px #0004"
    fontFamily: "{typography.mono.fontFamily}"
    fontSize: "12px"
    overflow: "hidden"
  terminal-bar:
    padding: "13px 16px"
    display: "flex"
    alignItems: "center"
    justifyContent: "space-between"
    borderBottom: "1px solid {colors.line}"
    color: "{colors.muted}"
    fontSize: "10px"
  terminal-body:
    padding: "22px 26px"
  terminal-prompt:
    color: "{colors.accent}"
    marginRight: "10px"
  terminal-answer:
    color: "{colors.muted}"
    fontSize: "12px"
  project-card:
    backgroundColor: "{colors.surface}"
    border: "1px solid {colors.line}"
    borderRadius: "{rounded.lg}"
    display: "flex"
    flexDirection: "column"
    transition: "border-color .2s, background .2s"
  project-card-hover:
    borderColor: "#677953"
    backgroundColor: "#1d241b"
  project-icon:
    fontFamily: "{typography.mono.fontFamily}"
    fontSize: "23px"
    color: "{colors.accent}"
  project-tag:
    fontFamily: "{typography.mono.fontFamily}"
    fontSize: "9px"
    letterSpacing: "1.2px"
    color: "{colors.muted}"
    border: "1px solid #3b4535"
    padding: "4px 8px"
    borderRadius: "4px"
  project-heading:
    fontFamily: "{typography.heading.fontFamily}"
    fontWeight: 500
    letterSpacing: "-1px"
    marginBottom: "17px"
  project-tech-item:
    fontFamily: "{typography.mono.fontFamily}"
    fontSize: "10px"
    padding: "3px 8px"
    borderRadius: "4px"
    backgroundColor: "#263020"
    color: "#c7d9b1"
  project-footer:
    marginTop: "auto"
    paddingTop: "18px"
    borderTop: "1px solid {colors.line}"
    display: "flex"
    justifyContent: "spaceBetween"
    gap: "12px"
    fontSize: "11px"
    color: "{colors.muted}"
  social-link:
    display: "flex"
    justifyContent: "spaceBetween"
    alignItems: "center"
    borderBottom: "1px solid {colors.line}"
    padding: "18px 0"
    fontSize: "21px"
    fontFamily: "{typography.heading.fontFamily}"
  social-link-hover:
    color: "{colors.accent}"
  social-link-label:
    display: "block"
    color: "{colors.muted}"
    fontFamily: "{typography.mono.fontFamily}"
    fontSize: "9px"
    letterSpacing: "1px"
    marginBottom: "3px"
  site-footer:
    borderTop: "1px solid {colors.line}"
    paddingBlock: "30px"
    display: "flex"
    alignItems: "center"
    justifyContent: "spaceBetween"
    gap: "24px"
  site-footer-text:
    fontSize: "11px"
    color: "{colors.muted}"
  site-footer-brand:
    fontSize: "19px"
  gif-card:
    maxWidth: "290px"
    margin: "35px 0 0"
    border: "1px solid {colors.line}"
    borderRadius: "8px"
    overflow: "hidden"
    backgroundColor: "{colors.surface}"
  gif-stage:
    height: "200px"
    display: "grid"
    placeItems: "center"
    backgroundColor: "#231d25"
  gif-image:
    height: "180px"
    width: "180px"
    objectFit: "contain"
    imageRendering: "pixelated"
    borderRadius: "8px"
  gif-caption:
    padding: "14px"
    display: "flex"
    alignItems: "center"
    justifyContent: "spaceBetween"
    gap: "8px"
    color: "{colors.muted}"
    fontFamily: "{typography.mono.fontFamily}"
    fontSize: "9px"
  gif-caption-link:
    textDecoration: "underline"
    textUnderlineOffset: "3px"
  gif-button:
    border: "1px solid #586747"
    backgroundColor: "transparent"
    color: "{colors.accent}"
    borderRadius: "4px"
    fontSize: "10px"
    padding: "9px"
    cursor: "pointer"
    whiteSpace: "nowrap"
  gif-button-hover:
    backgroundColor: "#293321"
  gif-button-hidden:
    display: "none"
overview:
  **Creative North Star: "The Terminal Explorer"**
  
  A developer portfolio that embraces the terminal aesthetic while remaining accessible and modern. The design treats the browser as a terminal window, incorporating familiar terminal elements like prompts, monospace text, and dark color schemes while maintaining web accessibility standards. The personality is curious, exploratory, and builder-focused - reflecting the mindset of someone who learns by taking things apart and rebuilding them better.
  
  Key Characteristics:
  - Dark terminal-inspired color palette with strategic accent highlights
  - Monospace and terminal-style UI elements throughout
  - Responsive design that works on both mobile and desktop
  - Accessibility features including skip links and focus outlines
  - Progressive enhancement with optional JavaScript
  - Subtle animations and interactions that enhance rather than distract
colors:
  **Character:** A dark terminal theme with a vibrant accent color that provides energy and highlights interactive elements.
  
  ### Primary
  - **Deep Terminal Black** (#111411): Main background color, creating the terminal window effect
  
  ### Surface
  - **Console Surface** (#191d18): Used for cards, panels, and elevated surfaces
  
  ### Text
  - **Terminal Text** (#eff2e9): Primary text color for high readability on dark backgrounds
  
  ### Muted
  - **Console Muted** (#a5afa0): Secondary text, borders, and less prominent elements
  
  ### Accent
  - **Terminal Green** (#c2f970): Interactive elements, highlights, and key visual accents
  
  ### Line
  - **Console Border** (#30382c): Dividers, borders, and subtle separation elements
  
  ### The Accent Rule
  - **The Terminal Green Rule.** The accent color (#c2f970) is used sparingly for interactive elements and key highlights, creating visual interest without overwhelming the dark terminal aesthetic.
typography:
  **Display Font:** Space Grotesk (with system-ui fallback)
  **Body Font:** DM Sans (with system-ui fallback)
  **Label/Mono Font:** ui-monospace, SFMono-Regular, Consolas, monospace
  
  **Character:** A clean, readable pairing where Space Grotesk provides modern heading character while DM Sans offers excellent body readability, complemented by authentic monospace for terminal elements and code.
  
  ### Hierarchy
  - **Display** (500, clamp(44px, 5.4vw, 72px), 1.1): Hero section title, creating impactful screen-filling typography
  - **Heading** (500, clamp(34px, 4vw, 49px), 1.1): Section titles throughout the site
  - **Title** (500, 27px, -1px): Subsection headings and project titles
  - **Body** (400, 16px, 1.7): Main paragraph text with comfortable line height
  - **Label** (varies, 10px-14px, varies): Labels, tags, and smaller UI elements
  
  ### The Hierarchy Rule
  - **The Readable Hierarchy Rule.** Heading sizes follow a clear, proportional scale that maintains readability across device sizes while preserving visual hierarchy.
layout:
  A centered, constrained layout approach with generous whitespace and responsive breakpoints. Content is centered in a container that maxes out at 1120px, with padding that adjusts based on screen size. The layout uses CSS Grid for complex sections like the hero (split between text and terminal visualization) and projects (multi-column grid that collapses to single column on mobile).
  
  Key spacing values create rhythm: 8px for tight spacing, 16px for standard, 22-26px for component padding, 30px for section padding, and 40-60px for larger gaps between major sections.
  
  Responsive behaviors include:
  - Hero section changing from two-column to single-column layout below 900px
  - Projects grid collapsing from two columns to one below 900px, then to one column with adjusted padding below 640px
  - About and contact sections shifting from two-column to single-column layouts at various breakpoints
  - Font sizes and spacing adjusting via clamp() and media queries for optimal readability
elevation & depth:
  This system primarily uses tonal layering through background color variations rather than shadows for depth. The main exception is the terminal component, which uses a subtle box-shadow to create lift and dimension. Most elevation is conveyed through background color contrasts between surfaces (#191d18) and the background (#111411).
  
  ### Shadow Vocabulary (if applicable)
  - **Terminal Lift** (`box-shadow: 20px 24px 80px #0004`): Applied to the terminal component to create a lifted, realistic terminal window effect
  
  ### The Elevation Rule
  - **The Subtle Shadow Rule.** Shadows are used sparingly and purposefully, primarily to enhance the terminal illusion rather than for general elevation.
shapes:
  A primarily rectilinear form language with strategic use of border radii to create visual interest and hierarchy. Straight edges dominate for a clean, terminal-like feel, while rounded corners are applied selectively to buttons, cards, and interactive elements to indicate affordance and create visual hierarchy.
  
  Corner strategy follows a scale from sharp (0px for most layout elements) to modest (5px for buttons) to more pronounced (8-12px for cards, containers, and special elements like the terminal). This creates a visual language where more interactive or elevated elements have slightly softer corners.
  
  Border usage is minimal but purposeful, primarily using the line color (#30382c) to define card borders, section separators, and interactive element states.
  
  ### The Corner Rule
  - **The Progressive Rounding Rule.** Border radius increases with element elevation and interactivity: layout elements use sharp corners, buttons get modest rounding, and cards/containers get more pronounced radii to convey depth and interactivity.
components:
  ### Buttons
  - **Shape:** Modest rounding (5px)
  - **Primary:** Terminal Green background with dark text, 13px 21px padding, 600 font weight
  - **Hover / Focus:** Background shifts to lighter green (#d5ff9b) with slight upward translation (-2px)
  - **Secondary / Ghost:** Transparent background with Terminal Text color, same padding and weight
  
  ### Terminal Component
  - **Style:** Dark surface with slight rotation and shadow for terminal window illusion
  - **Bar:** Divider with muted text showing prompt and working directory
  - **Body:** Monospace text area with prompt styling and answers
  - **Visual Elements:** Orbit visualization with planet (a_), stars, and exploratory label
  
  ### Project Cards
  - **Style:** Surface background with line-colored border
  - **Corner Style:** Pronounced rounding (9px)
  - **Background:** Console Surface color
  - **Border Strategy:** Line color border that changes on hover/focus
  - **Internal Padding:** Generous spacing (30px) that adjusts on smaller screens
  
  ### Social Links
  - **Style:** Horizontal links with bottom borders
  - **Typography:** Heading font, large size
  - **Default/Hover/Active States:** Color shifts to Accent on hover
  - **Mobile Treatment:** Stack vertically with adjusted spacing
  
  ### GIF Cards
  - **Style:** Container for the astronaut preview image
  - **Border:** Line-colored border with modest rounding (8px)
  - **Background:** Console Surface
  - **Image Treatment:** Pixelated rendering, constrained dimensions, circular mask effect via container
  - **Caption:** Space for attribution with link to source
  - **Controls:** Play button that appears on hover/focus states
  
  ### Skip Link
  - **Style:** Accessibility feature for keyboard navigation
  - **Background:** Accent color
  - **Text:** Background color for contrast
  - **Position:** Fixed top-left that animates into view on focus
  - **Padding:** Comfortable touch target size
do's and don'ts:
  ### Do:
  - **Do** use the Terminal Green accent (#c2f970) for interactive elements and key highlights
  - **Do** maintain proper color contrast between text and backgrounds for readability
  - **Do** use monospace fonts for terminal-style elements and code representations
  - **Do** include skip links for keyboard navigation accessibility
  - **Do** respect reduced motion preferences for users who need them
  - **Do** apply focus outlines using the Accent color for keyboard users
  
  ### Don't:
  - **Don't** use the Accent color for large background areas or text bodies
  - **Don't** remove focus outlines without providing alternative keyboard visibility
  - **Don't** use low-contrast color combinations that impair readability
  - **Don't** override browser default behaviors without providing equivalent functionality
  - **Don't** add unnecessary animations that could trigger vestibular disorders
  - **Don't** sacrifice accessibility for aesthetic preferences