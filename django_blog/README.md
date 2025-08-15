# Django Blog Application

A full-featured blog application built with Django that provides comprehensive blog post management, user authentication, and profile management capabilities.

## Features

### 🔐 Authentication System
- **User Registration**: New users can create accounts with email validation
- **Login/Logout**: Secure authentication with session management
- **User Profiles**: Customizable user profiles with avatar uploads and bio
- **CSRF Protection**: All forms are protected against CSRF attacks

### 📝 Blog Post Management (CRUD)
- **Create Posts**: Authenticated users can create new blog posts
- **View Posts**: Public access to view all blog posts and individual post details
- **Edit Posts**: Authors can edit their own posts
- **Delete Posts**: Authors can delete their own posts
- **Pagination**: Blog posts are paginated for better performance
- **Permission Control**: Only post authors can edit/delete their posts

### 💬 Comment System
- **Comment Model**: Ready-to-use comment system with timestamps
- **User Association**: Comments linked to users and posts
- **Timestamp Tracking**: Automatic creation and update timestamps

### 🎨 Modern UI/UX
- **Responsive Design**: Mobile-friendly responsive layout
- **Custom Styling**: Beautiful CSS styling for all components
- **Form Styling**: Consistent, modern form designs
- **Message System**: User feedback with success/error messages
- **Navigation**: Intuitive navigation with user-specific menu items

## Project Structure

```
django_blog/
├── django_blog/
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── blog/
│   ├── migrations/         # Database migrations
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css  # Custom CSS styles
│   │   └── js/
│   │       └── scripts.js  # JavaScript files
│   ├── templates/
│   │   ├── base.html       # Base template
│   │   ├── blog/           # Blog post templates
│   │   │   ├── post_list.html
│   │   │   ├── post_detail.html
│   │   │   ├── post_form.html
│   │   │   └── post_confirm_delete.html
│   │   └── registration/   # Authentication templates
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── register.html
│   │       └── profile.html
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── apps.py
│   ├── forms.py           # Custom forms
│   ├── models.py          # Data models
│   ├── urls.py            # App URL patterns
│   └── views.py           # View functions and classes
├── manage.py
└── README.md
```

## Models

### User Profile
- **User**: Extended Django User model
- **Profile**: One-to-one relationship with User
  - `bio`: TextField for user biography
  - `avatar`: ImageField for profile pictures

### Blog Post
- **Post**: Main blog post model
  - `title`: CharField for post title
  - `content`: TextField for post content
  - `published_date`: Auto-generated timestamp
  - `author`: ForeignKey to User model

### Comment System
- **Comment**: Comment model for blog posts
  - `post`: ForeignKey to Post
  - `author`: ForeignKey to User
  - `content`: TextField for comment content
  - `created_at`: Auto-generated creation timestamp
  - `updated_at`: Auto-updated modification timestamp

## URL Patterns

### Authentication URLs
- `/login/` - User login
- `/logout/` - User logout
- `/register/` - User registration
- `/profile/` - User profile management

### Blog Post URLs
- `/` - Home page (blog post list)
- `/posts/` - Blog post list
- `/posts/<int:pk>/` - Individual post detail
- `/posts/new/` - Create new post (authenticated users only)
- `/posts/<int:pk>/edit/` - Edit post (author only)
- `/posts/<int:pk>/delete/` - Delete post (author only)

## Views and Permissions

### Class-Based Views
- **PostListView**: Display paginated list of all posts
- **PostDetailView**: Display individual post details
- **PostCreateView**: Create new posts (LoginRequiredMixin)
- **PostUpdateView**: Edit posts (LoginRequiredMixin + UserPassesTestMixin)
- **PostDeleteView**: Delete posts (LoginRequiredMixin + UserPassesTestMixin)

### Function-Based Views
- **register**: User registration with automatic login
- **profile**: User profile view and edit functionality

### Permission System
- **Public Access**: Anyone can view blog posts
- **Authenticated Users**: Can create new posts and manage profiles
- **Authors Only**: Can edit/delete their own posts
- **CSRF Protection**: All forms include CSRF tokens

## Forms

### Authentication Forms
- **UserRegisterForm**: Extended UserCreationForm with email field
- **UserUpdateForm**: Update username and email
- **ProfileUpdateForm**: Update bio and avatar

### Blog Forms
- **PostForm**: Create and edit blog posts with custom styling

## Installation and Setup

### Prerequisites
- Python 3.8+
- Django 5.2+
- PostgreSQL (configured in settings)
- Pillow (for image handling)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django_blog
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow psycopg2-binary
   ```

4. **Database Setup**
   - Ensure PostgreSQL is running
   - Update database credentials in `settings.py`
   - Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Configuration

### Database Configuration
The project is configured to use PostgreSQL. Update the following in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files Configuration
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "blog" / "static"]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Security Settings
- CSRF middleware enabled
- Secure password hashers configured
- Debug mode for development only

## Usage

### For Users
1. **Registration**: Create a new account at `/register/`
2. **Login**: Access your account at `/login/`
3. **Profile**: Manage your profile at `/profile/`
4. **Create Posts**: Write new blog posts at `/posts/new/`
5. **Manage Posts**: Edit or delete your posts from the post detail page

### For Administrators
- Access Django admin at `/admin/`
- Manage users, posts, and profiles
- Monitor site activity and content

## Features in Detail

### User Authentication
- **Registration**: Email validation and duplicate checking
- **Login**: Session-based authentication with redirect
- **Profile Management**: Bio and avatar upload functionality
- **Auto Profile Creation**: Profiles automatically created for new users

### Blog Post Management
- **Rich Text Content**: Full text content support
- **Author Attribution**: Posts linked to their authors
- **Timestamp Tracking**: Automatic creation and update timestamps
- **Permission Control**: Authors can only edit their own posts

### UI/UX Features
- **Responsive Design**: Works on desktop and mobile devices
- **Modern Styling**: Clean, professional appearance
- **Form Validation**: Client and server-side validation
- **Message Feedback**: Success and error message display
- **Pagination**: Efficient handling of large post lists

## Security Features

- **CSRF Protection**: All forms include CSRF tokens
- **Authentication Required**: Protected routes for sensitive operations
- **Permission Checks**: Users can only modify their own content
- **Secure Password Handling**: Django's built-in password hashing
- **SQL Injection Protection**: Django ORM prevents SQL injection

## Development Notes

### Code Organization
- **Separation of Concerns**: Models, views, forms, and templates properly separated
- **DRY Principle**: Reusable components and base templates
- **Django Best Practices**: Following Django conventions and patterns

### Performance Considerations
- **Pagination**: Large datasets handled efficiently
- **Static File Optimization**: CSS and JS properly organized
- **Database Queries**: Optimized with select_related and prefetch_related where needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Check the Django documentation
- Review the code comments for implementation details

---

**Django Blog Application** - A comprehensive blogging platform built with Django, featuring modern UI, robust authentication, and full CRUD capabilities.
