# 🍽️ FoodGuard 🛒

For our CSIT327 course project, we are developing **FoodGuard**, a food waste management web application aimed at decreasing food waste. With this web-app, users can track the freshness of ingredients, manage them more effectively, and receive timely reminders before products expire. Additionally, users can integrate shopping lists to avoid unnecessary purchases, catalog ingredients, and get recipe suggestions based on what they already have, all through an easy-to-use interface.

## 📂 Repository Contents Overview

- [📊 Project Gantt Chart](https://docs.google.com/spreadsheets/d/11ZjoV7b2xWtxWbKaq-AH3ico476qVQgTe4zKd_bFd-s/edit?usp=sharing)
- [📝 Functional Business Requirements](https://docs.google.com/document/d/132jh_pLRHspBdgdF2ZyGM-lMcHAog-wezD5wm5X-SbY/edit?usp=sharing)
- [🖼️ Entity-Relationship Diagram](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=FOODGUARD-ERD.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1wjVtl0ysFldKHPq84wdmlHo09H5KyxjW%26export%3Ddownload)
- [🎨 UI/UX Mockup](https://www.figma.com/design/bxrI5SJgmKN9Yha5c0d4pz/FoodGuard?node-id=135-267&t=GAeqxJPBXLRVYOlj-1)
- Project Source Code

## 👥 Members

| Full Name                     | GitHub Profile                               |
| ----------------------------- | -------------------------------------------- |
| **Matunog**, Margaret Anne C. | [marginggg](https://github.com/margamatunog) |
| **Porter**, Nicolo Ryne A.    | [nicoryne](https://github.com/nicoryne)      |
| **San Diego**, Gabe Jeremy R. | [gabejeremy](https://github.com/gabejeremy)  |

## 🚀 Features

- **🔐 User Authentication and Management**

  - Provides secure login options for both registered users and guests. Registered users can save their data, while guest users can access core features temporarily. Users can also securely update their passwords and manage their account settings.

- **🍽️ Personalized Ingredients Dashboard**

  - Offers a dynamic home view displaying an overview of ingredients categorized by type (meat, fruits, vegetables, condiments) along with their freshness status.

- **🔔 User Notifications**

  - Users receive real-time notifications on updates from various features within the application, such as ingredients expiring, recipe book updates, and more.

- **📖 Recipe Book Feature**

  - Generates a list of recipe ideas based on the ingredients currently available in the user's inventory. Recipes are tailored to maximize the use of existing ingredients.

- **🛍️ Shopping List Integration**

  - Users can create and manage shopping lists based on their inventory needs and upcoming recipes.

- **🗣️ Text-to-Speech Integration**

  - Supports Text-to-Speech for hands-free dictation of ingredients and recipes.

## 🛠️ Installation Guide

> **Prerequisite:** Ensure Python 3.0 or higher is installed on your system.

### Step 1: Activate Virtual Environment

#### For Linux/macOS:

```bash
source ./env/bin/activate
```

#### For Windows:

```bash
source ./env/Scripts/activate
```

### Step 2: Install Dependencies

```bash
    pip install -r requirements.txt
```

### Step 3: Start the Django Development Server

```bash
    python manage.py runserver
```
