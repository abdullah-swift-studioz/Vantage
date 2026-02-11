#!/usr/bin/env python3
"""
Script to update navigation and footer across all HTML pages.
"""

import os
import re

# Define the new navigation for root-level pages
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
                            <a href="services/undergraduate.html" class="dropdown-item">
                                <div class="dropdown-title">Undergraduate Admissions</div>
                                <div class="dropdown-description">Ivy League & top university application support</div>
                            </a>
                            <a href="services/grad-school.html" class="dropdown-item">
                                <div class="dropdown-title">Graduate School Admissions</div>
                                <div class="dropdown-description">Masters & PhD program applications</div>
                            </a>
                            <a href="services/student-visa.html" class="dropdown-item">
                                <div class="dropdown-title">Student Visa Services</div>
                                <div class="dropdown-description">F-1 visa application & documentation</div>
                            </a>
                            <a href="services/fao-review.html" class="dropdown-item">
                                <div class="dropdown-title">FAO Application Review</div>
                                <div class="dropdown-description">Expert review by former admissions officers</div>
                            </a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a href="#" class="nav-link">About <span class="nav-arrow">▼</span></a>
                        <div class="nav-dropdown">
                            <a href="about.html" class="dropdown-item">
                                <div class="dropdown-title">About Us</div>
                                <div class="dropdown-description">Our story and mission</div>
                            </a>
                            <a href="results.html" class="dropdown-item">
                                <div class="dropdown-title">Our Results</div>
                                <div class="dropdown-description">Student success stories & outcomes</div>
                            </a>
                            <a href="press.html" class="dropdown-item">
                                <div class="dropdown-title">Press & Media</div>
                                <div class="dropdown-description">Vantage in the news</div>
                            </a>
                            <a href="careers.html" class="dropdown-item">
                                <div class="dropdown-title">Careers</div>
                                <div class="dropdown-description">Join our team</div>
                            </a>
                        </div>
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
        <a href="services/undergraduate.html" class="mobile-menu-link">Services</a>
        <a href="contact.html" class="mobile-menu-link">Contact</a>
        <a href="get-started.html" class="btn btn-primary" style="margin-top: 1rem;">Get Started</a>
        <button onclick="toggleMobileMenu()" style="position: absolute; top: 20px; right: 20px; background: none; border: none; font-size: 2rem;">✕</button>
    </div>'''

# Define the new footer for root-level pages
footer_root = '''<!-- Footer -->
    <footer class="site-footer">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; margin-bottom: 3rem;">
                <div>
                    <a href="index.html" style="text-decoration: none; display: inline-block; margin-bottom: 1.5rem;">
                        <div class="brand-logo" style="line-height: 1;">
                            <span style="font-family: 'Poppins', sans-serif; font-weight: 400; font-size: 2rem; color: white;">Vantage</span>
                            <span style="font-family: 'Poppins', sans-serif; font-weight: 400; font-size: 2rem; color: white; margin-left: 0.3rem;">Education</span>
                        </div>
                    </a>
                    <p style="opacity: 0.7; font-size: 0.9rem; line-height: 1.6;">Expert admissions consulting and student visa services for ambitious students.</p>
                </div>

                <div>
                    <h4 style="font-weight: 700; margin-bottom: 1.5rem;">Services</h4>
                    <ul style="list-style: none; opacity: 0.7; font-size: 0.9rem;">
                        <li style="margin-bottom: 0.8rem;"><a href="services/undergraduate.html" style="color: white; text-decoration: none;">Undergraduate Admissions</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="services/grad-school.html" style="color: white; text-decoration: none;">Graduate Admissions</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="services/student-visa.html" style="color: white; text-decoration: none;">Student Visa Services</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="services/fao-review.html" style="color: white; text-decoration: none;">FAO Review</a></li>
                    </ul>
                </div>

                <div>
                    <h4 style="font-weight: 700; margin-bottom: 1.5rem;">Company</h4>
                    <ul style="list-style: none; opacity: 0.7; font-size: 0.9rem;">
                        <li style="margin-bottom: 0.8rem;"><a href="about.html" style="color: white; text-decoration: none;">About Us</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="results.html" style="color: white; text-decoration: none;">Our Results</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="press.html" style="color: white; text-decoration: none;">Press</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="careers.html" style="color: white; text-decoration: none;">Careers</a></li>
                    </ul>
                </div>

                <div>
                    <h4 style="font-weight: 700; margin-bottom: 1.5rem;">Contact</h4>
                    <ul style="list-style: none; opacity: 0.7; font-size: 0.9rem;">
                        <li style="margin-bottom: 0.8rem;"><a href="get-started.html" style="color: white; text-decoration: none;">Get Started</a></li>
                        <li style="margin-bottom: 0.8rem;"><a href="contact.html" style="color: white; text-decoration: none;">Contact Us</a></li>
                    </ul>
                </div>
            </div>

            <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <p style="opacity: 0.5; font-size: 0.85rem; margin: 0;">&copy; 2025 Vantage Education. All rights reserved.</p>
                <div style="display: flex; gap: 2rem; opacity: 0.5; font-size: 0.85rem;">
                    <a href="terms.html" style="color: white; text-decoration: none;">Terms & Conditions</a>
                    <a href="privacy.html" style="color: white; text-decoration: none;">Privacy Policy</a>
                </div>
            </div>
        </div>
    </footer>'''

# Root-level HTML files to update
root_files = [
    'index.html',
    'about.html',
    'contact.html',
    'get-started.html',
    'press.html',
    'careers.html'
]

def update_file(filepath, nav_html, footer_html):
    """Update navigation and footer in a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace navigation (from <nav to end of mobile menu)
    nav_pattern = r'<nav class="navbar">.*?</div>\s*</div>\s*</nav>\s*<div class="mobile-menu-container".*?</div>'
    if re.search(nav_pattern, content, re.DOTALL):
        content = re.sub(nav_pattern, nav_html, content, flags=re.DOTALL)
        print(f"  ✓ Updated navigation in {filepath}")
    else:
        print(f"  ⚠ Could not find navigation pattern in {filepath}")
    
    # Replace footer (from <!-- Footer --> or <footer to </footer>)
    footer_pattern = r'(<!-- Footer -->[\s\S]*?)?<footer class="site-footer">[\s\S]*?</footer>'
    if re.search(footer_pattern, content):
        content = re.sub(footer_pattern, footer_html, content)
        print(f"  ✓ Updated footer in {filepath}")
    else:
        print(f"  ⚠ Could not find footer pattern in {filepath}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    base_dir = '/Users/abdullah/Downloads/vantage'
    
    print("Updating root-level pages...")
    for filename in root_files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            update_file(filepath, nav_root, footer_root)
        else:
            print(f"  ⚠ File not found: {filepath}")
    
    print("\nDone!")

if __name__ == "__main__":
    main()

