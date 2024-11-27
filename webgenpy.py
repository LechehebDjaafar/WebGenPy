import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import base64
import json


class ProfessionalWebsiteGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Professional Website Generator")
        master.geometry("700x900")
        master.configure(bg='#f4f4f4')

        # Style variables
        self.color_schemes = {
            'Modern Blue': {'primary': '#3498db', 'secondary': '#2980b9', 'text': '#333'},
            'Elegant Gray': {'primary': '#34495e', 'secondary': '#2c3e50', 'text': '#222'},
            'Vibrant Green': {'primary': '#2ecc71', 'secondary': '#27ae60', 'text': '#333'}
        }
        self.selected_color_scheme = tk.StringVar(value='Modern Blue')

        # Professional Sections
        self.sections = {
            'Education': [],
            'Work Experience': [],
            'Certifications': [],
            'Projects': []
        }

        self.create_ui()

    def create_ui(self):
        # Main Frame
        main_frame = tk.Frame(self.master, bg='#f4f4f4')
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Personal Information Section
        personal_frame = self.create_section(
            main_frame, "Personal Information")
        self.name_entry = self.add_entry(personal_frame, "Full Name:")
        self.title_entry = self.add_entry(
            personal_frame, "Professional Title:")
        self.email_entry = self.add_entry(
            personal_frame, "Professional Email:")
        self.phone_entry = self.add_entry(personal_frame, "Phone Number:")

        # Profile Picture
        profile_frame = self.create_section(main_frame, "Profile Picture")
        self.profile_pic_path = tk.StringVar()
        profile_pic_entry = tk.Entry(
            profile_frame, textvariable=self.profile_pic_path, width=50)
        profile_pic_entry.pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(profile_frame, text="Upload Picture",
                  command=self.upload_picture).pack(side=tk.LEFT, padx=5)

        # Professional Summary
        summary_frame = self.create_section(main_frame, "Professional Summary")
        self.summary_text = tk.Text(summary_frame, height=4, width=70)
        self.summary_text.pack(padx=5, pady=5)

        # Color Scheme Selection
        color_frame = self.create_section(main_frame, "Website Style")
        color_dropdown = tk.OptionMenu(
            color_frame, self.selected_color_scheme, *self.color_schemes.keys())
        color_dropdown.pack(padx=5, pady=5)

        # Professional Sections Management
        sections_frame = self.create_section(
            main_frame, "Professional Sections")
        for section_name in self.sections.keys():
            btn = tk.Button(sections_frame, text=f"Add {section_name}",
                            command=lambda name=section_name: self.add_section_dialog(name))
            btn.pack(side=tk.LEFT, padx=5)

        # Social Links
        social_frame = self.create_section(main_frame, "Social Links")
        self.linkedin_entry = self.add_entry(
            social_frame, "LinkedIn Profile URL:")
        self.github_entry = self.add_entry(social_frame, "GitHub Profile URL:")

        # Generate Website Button
        generate_btn = tk.Button(main_frame, text="Generate Professional Website",
                                 command=self.generate_website, bg='#3498db', fg='white')
        generate_btn.pack(pady=20)

    def create_section(self, parent, title):
        frame = tk.LabelFrame(parent, text=title, bg='#f4f4f4')
        frame.pack(fill=tk.X, pady=10)
        return frame

    def add_entry(self, parent, label):
        frame = tk.Frame(parent, bg='#f4f4f4')
        frame.pack(fill=tk.X, padx=5, pady=2)
        tk.Label(frame, text=label, bg='#f4f4f4').pack(side=tk.LEFT)
        entry = tk.Entry(frame, width=50)
        entry.pack(side=tk.RIGHT)
        return entry

    def upload_picture(self):
        filename = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        if filename:
            self.profile_pic_path.set(filename)

    def add_section_dialog(self, section_name):
        dialog = tk.Toplevel(self.master)
        dialog.title(f"Add {section_name}")

        # Inputs based on section type
        if section_name == "Education":
            self.create_education_dialog(dialog, section_name)
        elif section_name == "Work Experience":
            self.create_work_experience_dialog(dialog, section_name)
        elif section_name == "Certifications":
            self.create_certification_dialog(dialog, section_name)
        elif section_name == "Projects":
            self.create_project_dialog(dialog, section_name)

    def create_education_dialog(self, dialog, section_name):
        tk.Label(dialog, text="Institution").pack()
        institution_entry = tk.Entry(dialog)
        institution_entry.pack()

        tk.Label(dialog, text="Degree").pack()
        degree_entry = tk.Entry(dialog)
        degree_entry.pack()

        tk.Label(dialog, text="Graduation Year").pack()
        year_entry = tk.Entry(dialog)
        year_entry.pack()

        def save_education():
            education_data = {
                'institution': institution_entry.get(),
                'degree': degree_entry.get(),
                'year': year_entry.get()
            }
            self.sections[section_name].append(education_data)
            dialog.destroy()

        tk.Button(dialog, text="Save", command=save_education).pack(pady=10)

    def create_work_experience_dialog(self, dialog, section_name):
        tk.Label(dialog, text="Company").pack()
        company_entry = tk.Entry(dialog)
        company_entry.pack()

        tk.Label(dialog, text="Position").pack()
        position_entry = tk.Entry(dialog)
        position_entry.pack()

        tk.Label(dialog, text="Duration").pack()
        duration_entry = tk.Entry(dialog)
        duration_entry.pack()

        def save_work():
            work_data = {
                'company': company_entry.get(),
                'position': position_entry.get(),
                'duration': duration_entry.get()
            }
            self.sections[section_name].append(work_data)
            dialog.destroy()

        tk.Button(dialog, text="Save", command=save_work).pack(pady=10)

    def create_certification_dialog(self, dialog, section_name):
        tk.Label(dialog, text="Certification Name").pack()
        cert_entry = tk.Entry(dialog)
        cert_entry.pack()

        tk.Label(dialog, text="Issuing Organization").pack()
        org_entry = tk.Entry(dialog)
        org_entry.pack()

        def save_certification():
            cert_data = {
                'name': cert_entry.get(),
                'organization': org_entry.get()
            }
            self.sections[section_name].append(cert_data)
            dialog.destroy()

        tk.Button(dialog, text="Save",
                  command=save_certification).pack(pady=10)

    def create_project_dialog(self, dialog, section_name):
        tk.Label(dialog, text="Project Name").pack()
        name_entry = tk.Entry(dialog)
        name_entry.pack()

        tk.Label(dialog, text="Description").pack()
        desc_entry = tk.Text(dialog, height=3, width=30)
        desc_entry.pack()

        def save_project():
            project_data = {
                'name': name_entry.get(),
                'description': desc_entry.get("1.0", tk.END).strip()
            }
            self.sections[section_name].append(project_data)
            dialog.destroy()

        tk.Button(dialog, text="Save", command=save_project).pack(pady=10)


    def generate_website(self):
        # Validate required fields
        if not self.name_entry.get() or not self.profile_pic_path.get():
            messagebox.showerror("Error", "Name and Profile Picture are required!")
            return

        # Color scheme
        color_scheme = self.color_schemes[self.selected_color_scheme.get()]

        # Base64 encode profile picture
        with open(self.profile_pic_path.get(), "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        # Generate HTML with modern enhancements
        html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{self.name_entry.get()} - Professional Portfolio</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Animate.css for advanced animations -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" rel="stylesheet">
        <style>
            :root {{
                --primary-color: {color_scheme['primary']};
                --secondary-color: {color_scheme['secondary']};
                --text-color: {color_scheme['text']};
            }}
            body {{
                color: var(--text-color);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                scroll-behavior: smooth;
            }}
            /* Advanced Profile Image Styling */
            .profile-img {{
                max-width: 250px;
                border-radius: 50%;
                border: 5px solid var(--primary-color);
                transition: transform 0.3s ease-in-out;
                box-shadow: 0 10px 20px rgba(0,0,0,0.15);
            }}
            .profile-img:hover {{
                transform: scale(1.05);
            }}
            /* Section Animations */
            section {{
                opacity: 0;
                transform: translateY(20px);
                transition: opacity 0.6s ease-out, transform 0.6s ease-out;
            }}
            section.active {{
                opacity: 1;
                transform: translateY(0);
            }}
            /* Enhanced Navbar */
            .navbar {{
                backdrop-filter: blur(10px);
                background-color: rgba(52, 152, 219, 0.9) !important;
            }}
            .section-header {{
                color: var(--primary-color);
                border-bottom: 3px solid var(--primary-color);
                padding-bottom: 10px;
                margin-bottom: 20px;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            /* Professional List Styling */
            .professional-list .list-item {{
                background-color: rgba(52, 152, 219, 0.05);
                border-left: 4px solid var(--primary-color);
                padding: 15px;
                margin-bottom: 15px;
                transition: all 0.3s ease;
            }}
            .professional-list .list-item:hover {{
                transform: translateX(10px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <!-- Sticky Navbar -->
        <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
            <div class="container">
                <a class="navbar-brand" href="#">{self.name_entry.get()}</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="#experience">Experience</a></li>
                        <li class="nav-item"><a class="nav-link" href="#projects">Projects</a></li>
                        <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5 pt-5">
            <section id="about" class="text-center mb-5">
                <img src="data:image/jpeg;base64,{encoded_image}" class="profile-img mb-4" alt="Profile Picture" loading="lazy">
                <h1 class="animate__animated animate__fadeIn">{self.name_entry.get()}</h1>
                <h2 class="text-muted animate__animated animate__fadeIn animate__delay-1s">{self.title_entry.get()}</h2>
                <p class="lead animate__animated animate__fadeIn animate__delay-2s">{self.summary_text.get('1.0', tk.END).strip()}</p>
            </section>

            <section id="experience" class="my-5">
                <h3 class="section-header">Professional Experience</h3>
                <div class="professional-list">
                    {self.generate_section_html(
            self.sections['Work Experience'], 'work')}
                </div>
            </section>

            <section id="education" class="my-5">
                <h3 class="section-header">Education</h3>
                <div class="professional-list">
                    {self.generate_section_html(
                self.sections['Education'], 'education')}
                </div>
            </section>

            <section id="projects" class="my-5">
                <h3 class="section-header">Projects</h3>
                <div class="professional-list">
                    {self.generate_section_html(
                    self.sections['Projects'], 'projects')}
                </div>
            </section>

            <section id="certifications" class="my-5">
                <h3 class="section-header">Certifications</h3>
                <div class="professional-list">
                    {self.generate_section_html(
                        self.sections['Certifications'], 'certifications')}
                </div>
            </section>

<section id="contact" class="my-5 text-center">
    <h3 class="section-header mb-4">Contact Information</h3>
    <div class="row justify-content-center">
        <div class="col-md-6">
            <p class="mb-2">
                <strong>Email:</strong> 
                <a href="mailto:{self.email_entry.get()}" class="text-decoration-none">{self.email_entry.get()}</a>
            </p>
            <p class="mb-2">
                <strong>Phone:</strong> {self.phone_entry.get()}
            </p>
            <p class="mb-2">
                <strong>LinkedIn:</strong> 
                <a href="{self.linkedin_entry.get()}" target="_blank" class="text-decoration-none">View Profile</a>
            </p>
            <p>
                <strong>GitHub:</strong> 
                <a href="{self.github_entry.get()}" target="_blank" class="text-decoration-none">View Repositories</a>
            </p>
        </div>
    </div>
</section>

        </div>

        <!-- Bootstrap JS and dependencies -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script>
            // Scroll-triggered section animations
            document.addEventListener('DOMContentLoaded', function() {{
                const sections = document.querySelectorAll('section');
                const observerOptions = {{
                    root: null,
                    rootMargin: '0px',
                    threshold: 0.1
                }};

                const observer = new IntersectionObserver((entries) => {{
                    entries.forEach(entry => {{
                        if (entry.isIntersecting) {{
                            entry.target.classList.add('active');
                        }}
                    }});
                }}, observerOptions);

                sections.forEach(section => {{
                    observer.observe(section);
                }});
            }});
        </script>
    </body>
    </html>
        """

        # Save website
        save_dir = filedialog.askdirectory(
            title="Select Directory to Save Website")
        if save_dir:
            html_path = os.path.join(save_dir, "index.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            messagebox.showinfo(
                "Success", f"Professional website generated at {html_path}")

    def generate_section_html(self, data, section_type):
        if not data:
            return "<p>No entries available.</p>"

        html = ""
        for item in data:
            if section_type == 'work':
                html += f"""
                <div class="list-item">
                    <h4>{item['company']}</h4>
                    <p class="text-muted">{item['position']} | {item['duration']}</p>
                </div>
                """
            elif section_type == 'education':
                html += f"""
                <div class="list-item">
                    <h4>{item['institution']}</h4>
                    <p class="text-muted">{item['degree']} | Graduated {item['year']}</p>
                </div>
                """
            elif section_type == 'projects':
                html += f"""
                <div class="list-item">
                    <h4>{item['name']}</h4>
                    <p>{item['description']}</p>
                </div>
                """
            elif section_type == 'certifications':
                html += f"""
                <div class="list-item">
                    <h4>{item['name']}</h4>
                    <p class="text-muted">Issued by {item['organization']}</p>
                </div>
                """

        return html


def main():
    root = tk.Tk()
    ProfessionalWebsiteGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
