This Project is an example of how to create a AI API endpoints

             POST Request
                  │
                  ▼
        ┌───────────────────┐
        │ Django REST API   │
        │ /api/predict/     │
        └─────────┬─────────┘
                  │
                  ▼
        ┌───────────────────┐
        │ AI / ML Model     │
        │ RandomForest      │
        └─────────┬─────────┘
                  │
                  ▼
              Prediction
                  │
                  ▼
        ┌───────────────────┐
        │ JSON Response     │
        └───────────────────┘

AIProject
│
├── manage.py
│
├── AIProject
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── prediction
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    └── ...