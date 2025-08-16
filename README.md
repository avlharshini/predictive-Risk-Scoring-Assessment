# 🔐 Predictive Risk Scoring Assessment System

A comprehensive, production-ready Cybersecurity + AI/ML-based Predictive Risk Scoring System designed to outperform IBM QRadar UBA in flexibility, explainability, and real-time threat assessment.

## 🚀 Features

### Core Capabilities
- **Real-time Risk Assessment**: Dynamic risk scores (5-50) based on ML + rule-based analysis
- **ML-Powered Anomaly Detection**: Isolation Forest model for behavioral analysis
- **Comprehensive Rule Engine**: 10+ configurable security rules
- **Email Alert System**: Automated notifications for high-risk activities
- **Modern Web Dashboard**: React-based admin interface with real-time monitoring
- **Device Management**: Authorize/block devices with risk tracking
- **Session Logging**: Complete audit trail with CSV export

### Advanced Security Rules
- Failed login attempt tracking with automatic blocking
- USB usage + off-hours login detection
- Unauthorized access pattern recognition
- Unknown device login blocking
- Sensitive data access monitoring
- Network activity anomaly detection
- Excessive file access tracking
- Previous risk score consideration

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend│    │  FastAPI Backend│    │   ML Models     │
│                 │    │                 │    │                 │
│ • Dashboard     │◄──►│ • Risk Scoring  │◄──►│ • Isolation     │
│ • Alerts        │    │ • Rule Engine   │    │   Forest        │
│ • Device Mgmt   │    │ • Email Alerts  │    │ • Scaler        │
│ • Logs          │    │ • Session Store │    │ • Encoders      │
│ • Rule Editor   │    │ • API Endpoints │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory:**
```bash
cd backend
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Train the ML model:**
```bash
python train_model.py
```

4. **Start the FastAPI server:**
```bash
python app.py
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Install Node.js dependencies:**
```bash
npm install
```

3. **Start the React development server:**
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## 🔧 Configuration

### Email Alerts
Configure email settings in `backend/utils/email_utils.py`:
```python
SENDER_EMAIL = 'security@company.com'
SENDER_PASSWORD = 'your_password'
ADMIN_EMAILS = 'admin@company.com,security@company.com'
```

### Environment Variables
Create a `.env` file in the backend directory:
```env
SENDER_EMAIL=security@company.com
SENDER_PASSWORD=your_app_password
ADMIN_EMAILS=admin@company.com,security@company.com
```

## 📊 API Endpoints

### Core Endpoints
- `POST /evaluate` - Evaluate risk for a user session
- `GET /flagged-sessions` - Get all flagged sessions
- `GET /system-stats` - Get system statistics
- `POST /record-failed-login` - Record failed login attempt
- `GET /user-status/{user_id}` - Get user status

### Example API Usage
```bash
# Evaluate risk for a session
curl -X POST "http://localhost:8000/evaluate" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "U0001",
    "timestamp": "2024-01-15 10:30:00",
    "login_time": "10:00",
    "logout_time": "11:30",
    "files_accessed": 13,
    "sensitive_access": true,
    "unauthorized_access": 2,
    "usb_usage": 1,
    "location": "Remote",
    "network_activity": 0.92,
    "device_id": "DeviceB",
    "is_admin": false,
    "account_age_days": 1025,
    "login_method": "Password",
    "department": "Engineering",
    "off_hours_login": true,
    "known_device": false,
    "previous_risk_score": 36
  }'
```

## 🎯 Risk Scoring Algorithm

### ML Component (20 points max)
- Isolation Forest anomaly detection
- Feature engineering from behavioral data
- Normalized anomaly scores

### Rule-based Component (30 points max)
- Failed login attempts: 15 points
- USB + off-hours: 20 points
- Unauthorized access: 3 points per attempt
- Unknown device: 10 points
- Sensitive access: 8 points
- Off-hours login: 5 points
- High network activity: 5 points
- Excessive file access: 10 points max
- Previous high risk: 5 points

### Final Score Calculation
```
Final Score = ML Score (0-20) + Rule Score (0-30)
Max Score = 50 points
```

## 📈 Dashboard Features

### Real-time Monitoring
- Live risk score tracking
- System statistics overview
- Recent flagged sessions
- ML model status

### Analytics
- Risk distribution charts
- Time-series risk trends
- Department-wise analysis
- Device risk mapping

### Alert Management
- Priority-based filtering
- Email notification tracking
- Rule violation details
- Action recommendations

## 🔒 Security Features

### Authentication & Authorization
- Failed login attempt tracking
- Automatic user blocking
- Device authorization management
- Session monitoring

### Data Protection
- Sensitive access detection
- File access pattern analysis
- Network activity monitoring
- USB usage tracking

### Compliance & Auditing
- Complete session logging
- CSV export functionality
- Rule violation tracking
- Audit trail maintenance

## 🚀 Performance Optimizations

### Backend
- Async FastAPI endpoints
- In-memory rule engine
- Efficient ML model loading
- Optimized database queries

### Frontend
- React with Tailwind CSS
- Real-time data updates
- Responsive design
- Efficient state management

## 🧪 Testing

### Backend Testing
```bash
cd backend
python -m pytest tests/
```

### Frontend Testing
```bash
cd frontend
npm test
```

## 📝 Sample Data

The system includes a synthetic dataset with 10,000 entries featuring:
- Realistic user behaviors
- Anomaly patterns for ML training
- Various risk scenarios
- Department-specific patterns

## 🔄 Deployment

### Production Setup
1. Set up environment variables
2. Configure email SMTP settings
3. Set up database for session storage
4. Configure reverse proxy (nginx)
5. Set up SSL certificates
6. Configure monitoring and logging

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the documentation
- Review the API documentation at `/docs` when running

## 🔮 Future Enhancements

- [ ] Real-time WebSocket connections
- [ ] Advanced ML models (LSTM, Transformer)
- [ ] Integration with SIEM systems
- [ ] Mobile app for alerts
- [ ] Advanced analytics dashboard
- [ ] Multi-tenant architecture
- [ ] API rate limiting
- [ ] Advanced threat intelligence feeds

---

**Built with ❤️ for advanced cybersecurity risk assessment** 
