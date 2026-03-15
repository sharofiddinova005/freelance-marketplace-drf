\# Freelance Marketplace DRF (Mini Upwork)



\## Loyihaning maqsadi

Bu loyiha backend qismini ishlab chiqish orqali client va freelancerlar o‘rtasida loyiha, bid, contract va reviewlarni boshqarish imkonini beradi. Frontend hozircha mavjud emas, API Swagger / Postman orqali test qilinadi.



\## Texnologiyalar

\- Python 3.x

\- Django 6.x

\- Django REST Framework

\- PostgreSQL / SQLite (dev)

\- JWT Authentication

\- Git



\## API Endpointlar

\- \*\*Authentication\*\*

&#x20; - `POST /api/auth/register/`

&#x20; - `POST /api/auth/login/`

\- \*\*Project API\*\*

&#x20; - `POST /api/projects/`

&#x20; - `GET /api/projects/`

&#x20; - `GET /api/projects/<id>/`

\- \*\*Bid API\*\*

&#x20; - `POST /api/bids/`

&#x20; - `GET /api/bids/`

&#x20; - `GET /api/bids/project/<project\_id>/`

\- \*\*Contract API\*\*

&#x20; - `POST /api/contracts/accept-bid/<bid\_id>/`

&#x20; - `POST /api/contracts/<contract\_id>/finish/`

&#x20; - `GET /api/contracts/`

\- \*\*Review API\*\*

&#x20; - `POST /api/reviews/`

&#x20; - `GET /api/reviews/`

&#x20; - `GET /api/reviews/freelancer/<freelancer\_id>/`



\## Swagger / Redoc

\- Swagger: `http://127.0.0.1:8000/swagger/`

\- Redoc: `http://127.0.0.1:8000/redoc/`



\## Postman dokumentatsiya

\- Postman collection: (agar mavjud bo‘lsa, link qo‘ying)

\- Example: `freelance-marketplace-drf.postman\_collection.json`



\## Test foydalanuvchilar

\- \*\*Client\*\*

&#x20; - username: `client1`

&#x20; - password: `client123`

\- \*\*Freelancer\*\*

&#x20; - username: `freelancer1`

&#x20; - password: `freelancer123`



\## Loyihani ishga tushirish

1\. Repositoryni clone qilish:

&#x20;  ```bash

&#x20;  git clone https://github.com/sharofiddinova005/freelance-marketplace-drf.git

&#x20;  cd freelance-marketplace-drf

