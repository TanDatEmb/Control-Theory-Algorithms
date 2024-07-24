import os

# Đặt tên thư mục dự án
project_name = "ResearchProject"
base_path = os.path.join("D:\Control-Theory-Algorithms", project_name)

# Tạo các thư mục chính
os.makedirs(base_path, exist_ok=True)

# Danh sách các thư mục con
folders = [
    "Docs/ResearchPapers",
    "Docs/Reports",
    "Docs/Presentations",
    "MathModels/Equations",
    "MathModels/Simulations",
    "MathModels/Theories",
    "Code/Algorithms",
    "Code/Scripts",
    "Code/Tests",
    "Hardware/Schematics",
    "Hardware/PCB",
    "Hardware/Components",
    "Software/Interface",
    "Software/Libraries",
    "Software/Documentation",
    "Config/Settings",
    "Config/Environments",
    "Data/RawData",
    "Data/ProcessedData",
    "Experiments/Designs",
    "Experiments/Results",
    "Licenses"
]

for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Nội dung của các tệp README và LICENSE
readme_content = "# Project Name\n\nThis repository contains all resources for the embedded project."
license_content = "MIT License\n\nCopyright (c) {year} [Your Name]".format(year=2023)

# Tạo tệp README chính
with open(os.path.join(base_path, "README.md"), "w") as f:
    f.write(readme_content)

# Tạo tệp LICENSE
with open(os.path.join(base_path, "Licenses", "LICENSE"), "w") as f:
    f.write(license_content)

# Nội dung của các tệp README cho thư mục con
readme_files = {
    "Docs/README.md": "Documentation",
    "MathModels/README.md": "Mathematical Models",
    "Code/Algorithms/README.md": "Embedded Code",
    "Code/Scripts/README.md": "Software Code",
    "Hardware/README.md": "Hardware Designs",
    "Config/README.md": "Configuration Files",
    "Data/README.md": "Research Data",
    "Experiments/README.md": "Experiments"
}

for file_path, title in readme_files.items():
    with open(os.path.join(base_path, file_path), "w") as f:
        f.write(f"# {title}")

print(f"Project structure created successfully at {base_path}")
