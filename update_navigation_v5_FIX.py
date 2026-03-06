import os
import re

# Logic to calculate relative paths based on file depth
def get_relative_path(target_path, current_file_path):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.dirname(os.path.abspath(current_file_path))
    rel_path = os.path.relpath(os.path.join(root_dir, target_path), current_dir)
    return rel_path

def generate_nav_html(file_path):
    def rp(path): 
        return get_relative_path(path, file_path)

    nav_html = f'''    <!-- NEW NAVIGATION SYSTEM (V5 - EMERGENCY FIX) -->
    <nav class="navbar">
        <div class="nav-container">
            <!-- Logo (Desktop: White, Mobile: Handled in Overlay) -->
            <a href="{rp("index.html")}" class="nav-logo">
                <div class="brand-logo" style="line-height: 1;">
                    <span style="font-family: 'Poppins', sans-serif; font-weight: 400; font-size: 1.8rem; color: white;">Vantage</span>
                    <span style="font-family: 'Poppins', sans-serif; font-weight: 400; font-size: 1.8rem; color: white; margin-left: 0.3rem;">Education</span>
                </div>
            </a>

            <!-- Desktop Menu -->
            <ul class="nav-desktop">
                <!-- Services -->
                <li class="nav-item">
                    <a href="#" class="nav-link">Services <span class="nav-arrow">▼</span></a>
                    <div class="nav-dropdown">
                        <a href="{rp("services/country-selection.html")}" class="dropdown-item">
                            <span class="dropdown-title">Country Selection Counselling</span>
                            <span class="dropdown-description">Expert guidance on choosing the right country</span>
                        </a>
                        <a href="{rp("services/prepare-application.html")}" class="dropdown-item">
                            <span class="dropdown-title">Preparing Your Application</span>
                            <span class="dropdown-description">Complete application preparation</span>
                        </a>
                        <a href="{rp("services/apply-university.html")}" class="dropdown-item">
                            <span class="dropdown-title">Applying to University</span>
                            <span class="dropdown-description">End-to-end application support</span>
                        </a>
                        <a href="{rp("services/undergraduate.html")}" class="dropdown-item">
                            <span class="dropdown-title">Undergraduate Admissions</span>
                            <span class="dropdown-description">Ivy League & top university support</span>
                        </a>
                        <a href="{rp("services/grad-school.html")}" class="dropdown-item">
                            <span class="dropdown-title">Graduate School Admissions</span>
                            <span class="dropdown-description">Masters & PhD program applications</span>
                        </a>
                        <a href="{rp("services/student-visa.html")}" class="dropdown-item">
                            <span class="dropdown-title">Student Visa Services</span>
                            <span class="dropdown-description">F-1 visa application & documentation</span>
                        </a>
                        <a href="{rp("services/fao-review.html")}" class="dropdown-item">
                            <span class="dropdown-title">FAO Application Review</span>
                            <span class="dropdown-description">Expert review by former admissions officers</span>
                        </a>
                         <a href="{rp("services/transition-support.html")}" class="dropdown-item">
                            <span class="dropdown-title">Transition Support</span>
                            <span class="dropdown-description">Housing & landing support</span>
                        </a>
                    </div>
                </li>

                <!-- Countries -->
                <li class="nav-item">
                    <a href="#" class="nav-link">Countries <span class="nav-arrow">▼</span></a>
                    <div class="nav-dropdown" style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; min-width: 400px;">
                        <a href="{rp("countries/australia.html")}" class="dropdown-item"><span class="dropdown-title">Australia</span></a>
                        <a href="{rp("countries/canada.html")}" class="dropdown-item"><span class="dropdown-title">Canada</span></a>
                        <a href="{rp("countries/france.html")}" class="dropdown-item"><span class="dropdown-title">France</span></a>
                        <a href="{rp("countries/germany.html")}" class="dropdown-item"><span class="dropdown-title">Germany</span></a>
                        <a href="{rp("countries/ireland.html")}" class="dropdown-item"><span class="dropdown-title">Ireland</span></a>
                        <a href="{rp("countries/malaysia.html")}" class="dropdown-item"><span class="dropdown-title">Malaysia</span></a>
                        <a href="{rp("countries/new-zealand.html")}" class="dropdown-item"><span class="dropdown-title">New Zealand</span></a>
                        <a href="{rp("countries/singapore.html")}" class="dropdown-item"><span class="dropdown-title">Singapore</span></a>
                        <a href="{rp("countries/switzerland.html")}" class="dropdown-item"><span class="dropdown-title">Switzerland</span></a>
                        <a href="{rp("countries/uae.html")}" class="dropdown-item"><span class="dropdown-title">UAE</span></a>
                        <a href="{rp("countries/uk.html")}" class="dropdown-item"><span class="dropdown-title">UK</span></a>
                        <a href="{rp("countries/usa.html")}" class="dropdown-item"><span class="dropdown-title">USA</span></a>
                    </div>
                </li>

                <!-- About -->
                <li class="nav-item">
                    <a href="#" class="nav-link">About <span class="nav-arrow">▼</span></a>
                    <div class="nav-dropdown">
                        <a href="{rp("about.html")}" class="dropdown-item">
                            <span class="dropdown-title">About Us</span>
                            <span class="dropdown-description">Our story and values</span>
                        </a>
                        <a href="{rp("ceo-message.html")}" class="dropdown-item">
                            <span class="dropdown-title">CEO Message</span>
                            <span class="dropdown-description">A word from leadership</span>
                        </a>
                        <a href="{rp("mission-vision.html")}" class="dropdown-item">
                            <span class="dropdown-title">Mission & Vision</span>
                            <span class="dropdown-description">What drives us</span>
                        </a>
                        <a href="{rp("results.html")}" class="dropdown-item">
                            <span class="dropdown-title">Our Results</span>
                        </a>
                        <a href="{rp("press.html")}" class="dropdown-item">
                            <span class="dropdown-title">Press</span>
                        </a>
                         <a href="{rp("careers.html")}" class="dropdown-item">
                            <span class="dropdown-title">Careers</span>
                        </a>
                    </div>
                </li>

                <!-- Contact CTA -->
                <li>
                    <a href="{rp("contact.html")}" class="btn btn-primary">Contact</a>
                </li>
            </ul>

            <!-- Mobile Toggle -->
            <button class="mobile-nav-toggle" aria-label="Toggle navigation">
                <div class="hamburger-icon"></div>
            </button>
        </div>
    </nav>

    <!-- MOBILE MENU OVERLAY -->
    <div class="mobile-menu-overlay">
        <!-- Mobile Header (Logo + Close) -->
        <div class="mobile-menu-header">
            <a href="{rp("index.html")}" class="mobile-menu-logo">
                <span>Vantage</span>
                <span style="margin-top: -5px;">Education</span>
            </a>
            <!-- Close button is the toggler, positioned absolutely or relative, handled by JS active state -->
        </div>

        <ul class="mobile-nav-list">
            <li class="mobile-nav-item">
                <button class="mobile-nav-link" onclick="toggleMobileAccordion('mobile-services')">
                    Services <span class="mobile-arrow">▼</span>
                </button>
                <div id="mobile-services" class="mobile-dropdown-content">
                    <a href="{rp("services/country-selection.html")}" class="mobile-sublink">Country Selection</a>
                    <a href="{rp("services/prepare-application.html")}" class="mobile-sublink">Application Prep</a>
                    <a href="{rp("services/apply-university.html")}" class="mobile-sublink">Applying to Uni</a>
                    <a href="{rp("services/undergraduate.html")}" class="mobile-sublink">Undergraduate</a>
                    <a href="{rp("services/grad-school.html")}" class="mobile-sublink">Graduate School</a>
                    <a href="{rp("services/student-visa.html")}" class="mobile-sublink">Student Visa</a>
                    <a href="{rp("services/fao-review.html")}" class="mobile-sublink">FAO Review</a>
                    <a href="{rp("services/transition-support.html")}" class="mobile-sublink">Transition Support</a>
                </div>
            </li>
            
            <li class="mobile-nav-item">
                <button class="mobile-nav-link" onclick="toggleMobileAccordion('mobile-countries')">
                    Countries <span class="mobile-arrow">▼</span>
                </button>
                <div id="mobile-countries" class="mobile-dropdown-content" style="display: none; grid-template-columns: 1fr 1fr; gap: 10px;">
                    <a href="{rp("countries/australia.html")}" class="mobile-sublink">Australia</a>
                    <a href="{rp("countries/canada.html")}" class="mobile-sublink">Canada</a>
                    <a href="{rp("countries/france.html")}" class="mobile-sublink">France</a>
                    <a href="{rp("countries/germany.html")}" class="mobile-sublink">Germany</a>
                    <a href="{rp("countries/ireland.html")}" class="mobile-sublink">Ireland</a>
                    <a href="{rp("countries/malaysia.html")}" class="mobile-sublink">Malaysia</a>
                    <a href="{rp("countries/new-zealand.html")}" class="mobile-sublink">New Zealand</a>
                    <a href="{rp("countries/singapore.html")}" class="mobile-sublink">Singapore</a>
                    <a href="{rp("countries/switzerland.html")}" class="mobile-sublink">Switzerland</a>
                    <a href="{rp("countries/uae.html")}" class="mobile-sublink">UAE</a>
                    <a href="{rp("countries/uk.html")}" class="mobile-sublink">UK</a>
                    <a href="{rp("countries/usa.html")}" class="mobile-sublink">USA</a>
                </div>
            </li>

            <li class="mobile-nav-item">
                <button class="mobile-nav-link" onclick="toggleMobileAccordion('mobile-about')">
                    About <span class="mobile-arrow">▼</span>
                </button>
                <div id="mobile-about" class="mobile-dropdown-content">
                    <a href="{rp("about.html")}" class="mobile-sublink">About Us</a>
                    <a href="{rp("ceo-message.html")}" class="mobile-sublink">CEO Message</a>
                    <a href="{rp("mission-vision.html")}" class="mobile-sublink">Mission & Vision</a>
                    <a href="{rp("results.html")}" class="mobile-sublink">Results</a>
                    <a href="{rp("press.html")}" class="mobile-sublink">Press</a>
                    <a href="{rp("careers.html")}" class="mobile-sublink">Careers</a>
                </div>
            </li>

            <li class="mobile-nav-item">
                <a href="{rp("contact.html")}" class="mobile-nav-link" style="color: var(--crimson);">Contact Us</a>
            </li>
        </ul>
    </div>
    '''
    return nav_html

def process_files():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(subdir, file)
                print(f"Propessing: {file_path}")

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # EMERGENCY FIX STRATEGY:
                    # 1. Locate <body>.
                    # 2. Locate the first major content block (usually <section class="hero" or similar).
                    # 3. DELETE everything in between.
                    # 4. Insert V5 Nav.

                    # Regex to find everything between <body> and the start of the first section/main/header that IS NOT the nav
                    # We assume the "Hero" or main content starts with <section or <main or <div class="container"
                    
                    # Pattern: <body> ... [JUNK] ... <section
                    # We will use a loose match that captures the header area
                    
                    if '<body' in content:
                        # Find the insertion point (after body tag)
                        body_start = re.search(r'<body.*?>', content, re.IGNORECASE)
                        if not body_start:
                            print(f"Skipping {file}: No body tag found")
                            continue
                        
                        body_end_pos = body_start.end()
                        
                        # Find the start of the REAL content. 
                        # This is usually <section class="hero"> or <div class="hero"> or just <section>
                        # In the corrupted files, the junk is BEFORE this.
                        
                        # We look for the first occurrence of <section or <main after the body
                        content_start = re.search(r'<(section|main|div class="container")', content[body_end_pos:], re.IGNORECASE)
                        
                        if content_start:
                            real_content_start_pos = body_end_pos + content_start.start()
                            
                            # Everything between body_end_pos and real_content_start_pos is potentially JUNK
                            # We will replace it with the new nav
                            
                            pre_content = content[:body_end_pos]
                            post_content = content[real_content_start_pos:]
                            
                            new_nav = generate_nav_html(file_path)
                            
                            # Reassemble
                            new_content = pre_content + '\n' + new_nav + '\n    ' + post_content
                            
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                                
                        else:
                            # Fallback: strict regex replacement if no section found (e.g. small pages)
                            # Just look for the V2/V4 comments and nuke them
                            print(f"Fallback processing for {file} (no clear content start)")
                            # ... (Fallback logic if needed, but risky. Let's rely on the hero pattern for now as it covers 99% of pages)

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    process_files()
