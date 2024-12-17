# Project Description: Real Estate Management System

This project is a Django-based real estate management system designed to streamline the process of listing,
<br> 
browsing, and managing properties for rent and sale. It provides a user-friendly interface for property owners,
<br> 
agents, and users, facilitating seamless interactions between them. The system allows users to browse properties,
<br>
filter based on various criteria, save properties to wishlists, view details, and contact property owners.
<br>
Additionally, it includes features for subscriptions, ratings, property recommendations, and geolocation-based
<br>
searches to enhance the overall user experience.


##  Key Features

* <b> Realtors & Agents:</b> Dedicated features for property owners and realtors to manage their listings.
* <b> Best Sellers Section:</b> Highlights top-performing and popular properties.
* <b> Buy, Sell, Rent:</b> Users can buy, sell, or rent properties easily through the platform.
* <b> Wishlist:</b> Save your favorite properties for later viewing.
* <b> Ratings & Recommendations:</b> Rate properties and receive personalized recommendations.
* <b> Geolocation-Based Search:</b> Find properties near your location or within a specified area.
* <b> Subscription Services:</b> Exclusive access to premium property features through subscription.
* <b> User-Friendly Interface:</b> Easy navigation and intuitive design for a seamless experience.

## Technologies Used
* Backend: Django (Python)
* Frontend: HTML, CSS, JavaScript
* Database: MySQL (can be extended to PostgreSQL or SQLite)
* APIs: Django's internal APIs, geolocation APIs for distance calculations.
* Third-Party Libraries: Django Forms, Django Pagination, and Email backend for notifications.
<hr>

## How to run this project


1. **Clone the project**

```sh
git clone https://github.com/GUFRANHASANSPJ/UNIQUEPROPERTIES1.git
```

2.  **Make sure you are in *RateMyNest* folder**


3. **Active virtual environment (env)**
```sh
    env\scripts\activate
```

4. **install requirements**
```sh
pip install -r requirements.txt
```

5. **Run Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

```

6. **Run Server**

```sh
python manage.py runserver
```

7. **And Creating an admin user (superuser)**

```sh
python manage.py createsuperuser
```


<hr>
