# Contribution Guidelines

We welcome contributions from the community! To contribute to this project, please follow the steps below:

## How to Contribute

1. **Fork the Repository**  
   Click the "Fork" button on the top-right corner of the repository page to create a copy of this repository in your GitHub account.

2. **Clone Your Fork**  
   Clone your fork to your local machine using the following command:  
   ```bash
   git clone https://github.com/Eshetu21/ossp.git
   cd ossp
   ```
3. **Create a New Branch**
    Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature/your-feature-name
5. **Make Changes**
    Implement your changes in the appropriate files. Make sure to follow the existing code style.
6. **Test Your Changes**
    Before submitting your changes, ensure everything works as expected:
    Run the backend tests:
    ```bash
    pytest
    ```
    Run the frontend locally:
    ```bash
    npm run dev
7. **Commit Your Changes**
    Write a clear and descriptive commit message:
   ```bash
   git add .
   git commit -m "Add: Description of your changes
8. **Push Your Changes**
   Push your branch to your forked repository:
   ```bash
   git push origin feature/your-feature-name
9. **Open a Pull Request**
   Go to the original repository, click on "Pull Requests", and open a new pull request.
   Provide a clear description of the changes and link any related issues.
