from pathlib import Path
from setuptools import find_packages, setup

# Define the source root path
source_root = Path(".")

# Read the contents of the README file
readme_path = source_root / "C:/Users/Bharghavi/Downloads/ydata-profiling-develop/ydata-profiling-develop/README.md"
with readme_path.open(encoding="utf-8") as f:
    long_description = f.read()

# Read the requirements
requirements_path = source_root / "C:/Users/Bharghavi/Downloads/ydata-profiling-develop/ydata-profiling-develop/requirements.txt"
with requirements_path.open(encoding="utf8") as f:
    requirements = f.readlines()

# Read the version file
version_path = source_root / "C:/Users/Bharghavi/Downloads/ydata-profiling-develop/ydata-profiling-develop/VERSION"
try:
    version = version_path.read_text().rstrip("\n")
except FileNotFoundError:
    version = "0.0.dev0"

# Ensure the directory structure exists for version.py
version_dir = source_root / "src/ydata_profiling"
version_dir.mkdir(parents=True, exist_ok=True)

# Write the version file in the src directory
version_file_path = version_dir / "version.py"
with version_file_path.open("w") as version_file:
    version_file.write(f"__version__ = '{version}'")

# Define the setup configuration
setup(
    name="ydata-profiling",
    version=version,
    author="YData Labs Inc",
    author_email="opensource@ydata.ai",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/ydataai/ydata-profiling",
    license="MIT",
    description="Generate profile report for pandas DataFrame",
    python_requires=">=3.7, <3.13",
    install_requires=requirements,
    extras_require={
        "notebook": [
            "jupyter-client>=5.3.4",
            "jupyter-core>=4.6.3",
            "ipywidgets>=7.5.1",
        ],
        "unicode": [
            "tangled-up-in-unicode==0.2.0",
        ],
    },
    package_data={
        "ydata_profiling": ["py.typed"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering",
        "Framework :: IPython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="pandas data-science data-analysis python jupyter ipython",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "ydata_profiling = ydata_profiling.controller.console:main",
            "pandas_profiling = ydata_profiling.controller.console:main",
        ]
    },
    options={"bdist_wheel": {"universal": True}},
)
