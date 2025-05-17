# Shop Project Django

This is a Django-based e-commerce project designed to manage an online shop. Below is an overview of the project and its features.

## Features

- User authentication and registration
- Product listing and categorization
- Shopping cart functionality
- Order management
- Payment gateway integration
- Admin panel for managing products, orders, and users

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Shop_project_django.git
    cd Shop_project_django
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage the shop.

## Folder Structure

```
Shop_project_django/
├── shop/               # Main application folder
├── users/              # User management app
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [amin138400138400@gmail.com].