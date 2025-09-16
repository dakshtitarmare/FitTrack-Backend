# FitTrack Backend

FitTrack Backend is a Flask-based application designed to manage and display QR code data for product parts. It integrates with Supabase for data storage and retrieval, providing a seamless backend solution for QR code-based inventory management.

---

## Features

- **Save QR Data**: Accepts QR data via a REST API and stores it in a Supabase database.
- **Display QR Data**: Fetches and displays QR data in a user-friendly HTML template.
- **Supabase Integration**: Uses Supabase as the backend database for storing and retrieving data.
- **Dynamic HTML Templates**: Renders data dynamically using Flask's Jinja2 templating engine.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- Supabase account and API credentials

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dakshtitarmare/FitTrack-Backend.git
   cd FitTrack-Backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:

   - Create a `.env` file in the root directory (if not already present).
   - Add your Supabase credentials:

     ```properties
     SUPABASE_URL=<your_supabase_url>
     SUPABASE_API_KEY=<your_supabase_api_key>
     SUPABASE_TABLE=qr_data
     ```

---

## Usage

1. **Run the Flask application**:

   ```bash
   python app.py
   ```

2. **API Endpoints**:

   - **Save QR Data**: `POST /api/save_qr_data`
     - Request Body (JSON):
       ```json
       {
         "partType": "Part Type",
         "serialNo": "Serial Number",
         "vendorId": "Vendor ID",
         "mfgDate": "Manufacturing Date",
         "lotNo": "Lot Number",
         "warrantyPeriod": "Warranty Period"
       }
       ```
     - Response:
       ```json
       {
         "uid": "Generated UID"
       }
       ```

   - **Show QR Data**: `GET /showdata/<uid>`
     - Displays the data for the given UID in an HTML template.

3. **Access the Application**:

   - Open your browser and navigate to `http://127.0.0.1:5000`.

---

## File Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── .gitignore             # Git ignore file
├── templates/             # HTML templates
│   ├── show_data.html     # Template for displaying QR data
```

---

## Templates

- **`show_data.html`**: Displays QR data in a visually appealing format.

---

## Environment Variables

The `.env` file contains the following variables:

- `SUPABASE_URL`: Your Supabase project URL.
- `SUPABASE_API_KEY`: Your Supabase API key.
- `SUPABASE_TABLE`: The name of the table where QR data is stored.

---

## Dependencies

The project uses the following Python libraries:

- Flask
- python-dotenv
- requests
- qrcode
- matplotlib
- numpy
- scipy

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

- **Daksh Titarmare**  
  GitHub: [dakshtitarmare](https://github.com/dakshtitarmare)

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## Acknowledgments

- [Supabase](https://supabase.com) for providing an easy-to-use backend solution.
- Flask for its simplicity and flexibility.