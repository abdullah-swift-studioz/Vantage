#!/usr/bin/env python3
"""
Script to update navigation across all HTML pages with new structure.
"""

import os
import re

# New navigation for root-level pages
nav_root = '''<nav class="navbar">
        <div class="nav-container">
            <div class="nav-left">
                <a href="index.html" class="nav-logo" style="text-decoration: none;">
                    <div class="brand-logo" style="line-height: 1;">
                        <span style="font-family: 'Poppins', sans-serif; font-weight: 400; font-size: 1.8rem; color: white;">Vantage</span>
                        <span style="font-family: 'Poppins', sans-serif; font-weight: 400; font-size: 1.8rem; color: white; margin-left: 0.3rem;">Education</span>
                    </div>
                </a>

                <ul class="nav-menu">
                    <li class="nav-item">
                        <a href="#" class="nav-link">Services <span class="nav-arrow">▼</span></a>
                        <div class="nav-dropdown">
                            <a href="services/country-selection.html" class="dropdown-item">
                                <div class="dropdown-title">Country Selection Counselling</div>
                                <div class="dropdown-description">Expert guidance on choosing the right country for your studies</div>
                            </a>
                            <a href="services/prepare-application.html" class="dropdown-item">
                                <div class="dropdown-title">Preparing Your University Application</div>
                                <div class="dropdown-description">Complete application preparation and documentation</div>
                            </a>
                            <a href="services/apply-university.html" class="dropdown-item">
                                <div class="dropdown-title">Applying to Your Dream University</div>
                                <div class="dropdown-description">End-to-end application submission support</div>
                            </a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a href="#" class="nav-link">About <span class="nav-arrow">▼</span></a>
                        <div class="nav-dropdown">
                            <a href="about.html" class="dropdown-item">
                                <div class="dropdown-title">About the Company</div>
                                <div class="dropdown-description">Our story and background</div>
                            </a>
                            <a href="ceo-message.html" class="dropdown-item">
                                <div class="dropdown-title">Message from our CEO</div>
                                <div class="dropdown-description">A personal message from our leadership</div>
                            </a>
                            <a href="mission-vision.html" class="dropdown-item">
                                <div class="dropdown-title">Mission & Vision</div>
                                <div class="dropdown-description">Our mission and vision for the future</div>
                            </a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a href="why-choose-us.html" class="nav-link">Why Choose Us</a>
                    </li>
                    <li class="nav-item">
                        <a href="terms.html" class="nav-link">Terms & Conditions</a>
                    </li>
                    <li class="nav-item">
                        <a href="contact.html" class="nav-link">Contact</a>
                    </li>
                </ul>
            </div>

            <div class="nav-right" style="display: flex; align-items: center; gap: 1rem;">
                <a href="get-started.html" class="btn btn-primary nav-cta">Get Started</a>
                <button class="mobile-menu-btn" onclick="toggleMobileMenu()">☰</button>
            </div>
        </div>
    </nav>

    <div class="mobile-menu-container" id="mobileMenu">
        <a href="index.html" class="mobile-menu-link">Home</a>
        <a href="about.html" class="mobile-menu-link">About</a>
        <a href="services/country-selection.html" class="mobile-menu-link">Services</a>
        <a href="why-choose-us.html" class="mobile-menu-link">Why Choose Us</a>
        <a href="terms.html" class="mobile-menu-link">Terms & Conditions</a>
        <a href="contact.html" class="mobile-menu-link">Contact</a>
        <a href="get-started.html" class="btn btn-primary" style="margin-top: 1rem;">Get Started</a>
        <button onclick="toggleMobileMenu()" style="position: absolute; top: 20px; right: 20px; background: none; border: none; font-size: 2rem;">✕</button>
    </div>'''

# Navigation for services pages (with ../ paths)
nav_services = nav_root.replace('href="services/', 'href="').replace('href="about.html"', 'href="../about.html"').replace('href="ceo-message.html"', 'href="../ceo-message.html"').replace('href="mission-vision.html"', 'href="../mission-vision.html"').replace('href="why-choose-us.html"', 'href="../why-choose-us.html"').replace('href="terms.html"', 'href="../terms.html"').replace('href="contact.html"', 'href="../contact.html"').replace('href="get-started.html"', 'href="../get-started.html"').replace('href="index.html"', 'href="../index.html"').replace('href="services/country-selection.html"', 'href="country-selection.html"').replace('href="services/prepare-application.html"', 'href="prepare-application.html"').replace('href="services/apply-university.html"', 'href="apply-university.html"')

def update_file(filepath, nav_html):
    """Update navigation in a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace navigation (from <nav to end of mobile menu)
    nav_pattern = r'<nav class="navbar">.*?</div>\s*</div>\s*</nav>\s*<div class="mobile-menu-container".*?</div>'
    if re.search(nav_pattern, content, re.DOTALL):
        content = re.sub(nav_pattern, nav_html, content, flags=re.DOTALL)
        print(f"  ✓ Updated navigation in {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print(f"  ⚠ Could not find navigation pattern in {filepath}")
        return False

def main():
    base_dir = '/Users/abdullah/Downloads/vantage'
    
    print("Updating root-level pages...")
    root_files = [
        'index.html',
        'about.html',
        'contact.html',
        'get-started.html',
        'press.html',
        'careers.html',
        'results.html',
        'terms.html',
        'privacy.html'
    ]
    
    for filename in root_files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            update_file(filepath, nav_root)
        else:
            print(f"  ⚠ File not found: {filepath}")
    

    print("\nUpdating services pages...")
    services_dir = os.path.join(base_dir, 'services')
    if os.path.exists(services_dir):
        for filename in os.listdir(services_dir):
            if filename.endswith('.html'):
                filepath = os.path.join(services_dir, filename)
                update_file(filepath, nav_services)
    
    print("\nUpdating countries pages...")
    countries_dir = os.path.join(base_dir, 'countries')
    if os.path.exists(countries_dir):
        for filename in os.listdir(countries_dir):
            if filename.endswith('.html'):
                filepath = os.path.join(countries_dir, filename)
                # reuse nav_services as it uses ../ structure which is same for countries/
                update_file(filepath, nav_services)
    
    print("\nDone!")

if __name__ == "__main__":
    main()

