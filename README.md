# 🏗️ Automated WordPress Deployment System 🚀

## 📖 Overview  
This project automates the **deployment of WordPress websites** on an Ubuntu server using an **HTML form**, **Apache**, **MySQL**, **Flask**, and **WP-CLI**.  

Users can submit a domain name via a web form, triggering a **Flask backend** that executes an automation script to set up the WordPress site **without manual intervention**.  

---

## 🔧 Technologies Used  
- **Ubuntu Server** – Hosting the web applications  
- **Apache** – Handles domain requests & proxies requests to Flask  
- **Flask (Python)** – Processes form submissions and executes automation scripts  
- **MySQL** – Database setup for WordPress  
- **PHP** – Required for WordPress functionality  
- **WP-CLI** – Command-line interface to automate WordPress installation  

---

## 🔀 System Architecture & Flowchart  

```mermaid
graph TD;
    A[User submits form] -->|Request sent| B[Apache Server];
    B -->|Forwards to| C[Flask App];
    C -->|Executes| D[Automation Script];
    D -->|Sets up| E[Apache Virtual Host & MySQL DB];
    E -->|Deploys| F[WordPress using WP-CLI];
    F -->|Returns success message| G[Flask App];
    G -->|Displays success on web UI| H[User]
