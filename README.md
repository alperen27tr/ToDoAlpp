# ToDoList Web Application

This project is a ToDo list application developed using Django for the backend and React for the frontend.

## Features

- **User Management:** Users can sign up, log in, and manage their profiles.
- **Category Management:** Tasks can be organized by categories.
- **Task Management:** Users can add, edit, and mark tasks as completed.
- **Database:** Tasks and user data are stored in an SQLite database.
- **Dynamic Menus:** User-specific task lists and category menus are dynamically displayed.

## Installation

### Requirements

- Python 3.x
- Node.js
- Django 3.x or higher
- React 17.x or higher

### Backend (Django) Setup

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Migrate the database:

    ```bash
    python manage.py migrate
    ```

3. Start the server:

    ```bash
    python manage.py runserver
    ```

### Frontend (React) Setup

1. Install the required Node.js packages:

    ```bash
    npm install
    ```

2. Start the React application:

    ```bash
    npm start
    ```

## Usage

- The backend server runs on `http://localhost:8000/` by default.
- The frontend application runs on `http://localhost:3000/` by default.

## API Endpoints

- **Users:** `http://localhost:8000/users/`
- **Categories:** `http://localhost:8000/categories/`
- **Todos:** `http://localhost:8000/todos/`

## Contributing

If you would like to contribute, please submit a pull request or open an issue. All contributions are welcome.

## License

This project is licensed under the MIT License.


-----------------------------------------------------------------------------


# ToDoList Web Uygulaması

Bu proje, Django backend ve React frontend kullanılarak geliştirilmiş bir ToDo listesi uygulamasıdır.

## Özellikler

- **Kullanıcı Yönetimi:** Kullanıcılar kaydolabilir, giriş yapabilir ve profillerini yönetebilir.
- **Kategori Yönetimi:** Görevler kategorilere göre düzenlenebilir.
- **Görev Yönetimi:** Kullanıcılar görev ekleyebilir, düzenleyebilir ve tamamlanmış olarak işaretleyebilir.
- **Veritabanı:** Görevler ve kullanıcı verileri SQLite veritabanında saklanır.
- **Dinamik Menüler:** Kullanıcıya özel görev listeleri ve kategori menüleri dinamik olarak görüntülenir.

## Kurulum

### Gereksinimler

- Python 3.x
- Node.js
- Django 3.x veya üzeri
- React 17.x veya üzeri

### Backend (Django) Kurulumu

1. Gerekli Python paketlerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

2. Veritabanını migrate edin:

    ```bash
    python manage.py migrate
    ```

3. Sunucuyu başlatın:

    ```bash
    python manage.py runserver
    ```

### Frontend (React) Kurulumu

1. Gerekli Node.js paketlerini yükleyin:

    ```bash
    npm install
    ```

2. React uygulamasını başlatın:

    ```bash
    npm start
    ```

## Kullanım

- Backend sunucusu varsayılan olarak `http://localhost:8000/` adresinde çalışır.
- Frontend uygulaması varsayılan olarak `http://localhost:3000/` adresinde çalışır.

## API Endpoints

- **Kullanıcılar:** `http://localhost:8000/users/`
- **Kategoriler:** `http://localhost:8000/categories/`
- **Görevler:** `http://localhost:8000/todos/`

## Katkıda Bulunma

Katkıda bulunmak isterseniz, bir pull request gönderin veya bir sorun bildirisi açın. Tüm katkılar memnuniyetle karşılanır.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.



