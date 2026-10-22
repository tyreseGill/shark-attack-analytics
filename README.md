<div align="center">
    <h1>Shark Attack Analytics</h1>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#about-the-project">About the Project</a>
    </li>
    <li>
        <a href="#documentation">Documentation</a>
    </li>
    <li>
        <a href="#getting-started">Getting Started</a>
    </li>
    <li>
        <a href="#acknowledgements">Acknowledgements</a>
    </li>
  </ol>
</details>

## About the Project
Shark Attack Analytics is a data-driven web application built to explore and visualize thousands of historical shark attack records. The project will combine data preprocessing, PostgreSQL storage, geospatial mapping, and interactive Plotly dashboards to uncover trends in attack frequency, location, victim activity, shark species, and incident outcomes. Users will be able to filter and analyze data through dynamic visualizations designed to support exploratory analysis and storytelling.

### Built With

#### Programming Languages
- [![Python][Python-icon]][Python-url]
<!-- - [![JavaScript][JavaScript-icon]][JavaScript-url]
- [![CSS][CSS-icon]][CSS-url] -->
- [![Jupyter][Jupyter-icon]][Jupyter-url]

<!-- #### Databases
- [![Postgres][Postgres-icon]][Postgres-url] -->

<!-- #### Frameworks
- [![Node.js][Node.js-icon]][Node.js-url]
- [![Express.js][Express.js-icon]][Express.js-url] -->


## Documentation
Additional project documentation is available in the [docs/](./docs/dataset_overview.ipynb) folder:
- [Exploratory Dataset Analysis](docs/dataset_overview.ipynb)


## Getting Started

### Prerequisites
Before starting, ensure the following software is installed:  

- Node.js
- PostgreSQL

> [!TIP]
> Installation instructions can be found through The Odin Project:
>
> - Node.js: https://www.theodinproject.com/lessons/foundations-installing-node-js
> - PostgreSQL: https://www.theodinproject.com/lessons/nodejs-installing-postgresql

### Installation
1. Clone the repository
    - `git clone <REPOSITORY_URL>`
    - `cd shark-attack-analytics`
2. Run the following to install the necessary dependencies:
    - `npm install dotenv`
    - `npm install express`
    - `npm init -y`
    - `npm install`
    - `npm install react-plotly.js plotly.js`

<!-- ### Usage -->

### Environment Configuration
Create a `.env` file with this structure:
```
SERVER_PORT=<server-port>
DATABASE_CONNECTION_STRING=<postgres://{username}:{password}@localhost:{database-port}/{database-name}>
```

> [!IMPORTANT]
> The database name created from database setup must match the value specified in the above `DATABASE_CONNECTION_STRING`.

As an example, the `.env` file might look something like this:
```
SERVER_PORT=3000
DATABASE_CONNECTION_STRING=postgres://user:12345@localhost:5432/db
```

> [!IMPORTANT]
> - `DATABASE_CONNECTION_STRING` allows the app to connect to a PostgreSQL database.

<!-- ### Database Setup
1. Open the PostgreSQL shell by running `psql`.
2. Create a database with `CREATE DATABASE database_name;`.
3. Exit with `\q`. -->

## Acknowledgements
[![Kaggle][Kaggle-icon]][Kaggle-url]

- This project utilizes the **Shark attack dataset** by [Felipe_Esc](https://www.kaggle.com/felipeesc).

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Programming Languages -->
[CSS-icon]: https://img.shields.io/badge/CSS-639?style=for-the-badge&logo=css&logoColor=fff
[CSS-url]: https://developer.mozilla.org/en-US/docs/Web/CSS
[JavaScript-icon]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[Jupyter-icon]: https://img.shields.io/badge/Jupyter-ffffff?style=for-the-badge&logo=Jupyter
[Jupyter-url]: https://jupyter.org/
[Python-icon]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

<!-- Databases -->
[Postgres-icon]: https://img.shields.io/badge/Postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/

<!-- Frameworks -->
[Node.js-icon]: https://img.shields.io/badge/Node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white
[Node.js-url]: https://nodejs.org/
[Express.js-icon]: https://img.shields.io/badge/Express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB
[Express.js-url]: https://expressjs.com/

<!-- Acknowledgements -->
[Kaggle-icon]: https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=fff
[Kaggle-url]: https://www.kaggle.com/datasets/felipeesc/shark-attack-dataset/
