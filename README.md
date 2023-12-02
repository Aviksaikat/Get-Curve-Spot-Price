<div align="center">
    <h1>Get-Curve-Spot-Price</h1>
</div>
<div align="center">
<p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry" />
    <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest" />

</p>
    <img src="https://img.shields.io/github/license/Aviksaikat/Get-Curve-Spot-Price?style=flat&color=E8FF00" alt="GitHub license" />
    <img src="https://img.shields.io/github/last-commit/Aviksaikat/Get-Curve-Spot-Price?style=flat&color=E8FF00" alt="git-last-commit" />
    <img src="https://img.shields.io/github/commit-activity/m/Aviksaikat/Get-Curve-Spot-Price?style=flat&color=E8FF00" alt="GitHub commit activity" />
    <img src="https://img.shields.io/github/languages/top/Aviksaikat/Get-Curve-Spot-Price?style=flat&color=E8FF00" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📂 repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running Get-Curve-Spot-Price](#-running-Get-Curve-Spot-Price)
    - [🧪 Tests](#-tests)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Get the spot price of any token pair listed on [curve](https://curve.fi/).


## 📂 Repository Structure

```sh
└── Get-Curve-Spot-Price/
    ├── .build/
    │   ├── ICurvePool.json
    │   ├── IDAI.json
    │   ├── IERC20.json
    │   ├── IMATIC.json
    │   ├── IUSDC.json
    │   ├── IWBTC.json
    │   ├── IWETH.json
    │   └── __local__.json
    ├── ape-config.yaml
    ├── contracts/
    │   └── interfaces/
    │       ├── ICurvePool.sol
    │       ├── IDAI.sol
    │       ├── IERC20.sol
    │       ├── IMATIC.sol
    │       ├── IUSDC.sol
    │       ├── IWBTC.sol
    │       └── IWETH.sol
    ├── poetry.lock
    ├── pyproject.toml
    └── scripts/
        ├── constants.py
        ├── get_price.py
        ├── tokens.py
        └── utils.py
```

---


### 🔧 Installation

1. Clone the Get-Curve-Spot-Price repository:
```sh
git clone https://github.com/Aviksaikat/Get-Curve-Spot-Price
```

2. Change to the project directory:
```sh
cd Get-Curve-Spot-Price
```

3. Install the dependencies:

- install [poetry](https://python-poetry.org/)

```sh
poetry install
```

### 🤖 Running Get-Curve-Spot-Price

```sh
poery ape run scripts/get_price.py

# Or
poetry shell
ape run scripts/get_price.py
```

### 🧪 Tests
```sh
poery ape test
```

---


## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Aviksaikat/Get-Curve-Spot-Price/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Aviksaikat/Get-Curve-Spot-Price/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Aviksaikat/Get-Curve-Spot-Price/issues)**: Submit bugs found or log feature requests for AVIKSAIKAT.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---



---

## 👏 Acknowledgments

- [Aviksaikat](https://github.com/aviksaikat)

[**Return**](#Top)

---