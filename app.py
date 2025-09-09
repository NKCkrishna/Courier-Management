import streamlit as st
import pymysql
import streamlit.components.v1 as components

# Database connection
def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='823f2987c3b2',
        database='courier_db'
    )
    return connection

# Frontend code for the homepage
def home_page():
    st.title("Courier Management System")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Register", "Login", "Dashboard"])

    if page == "Home":
        st.write("Welcome to the Courier Management System")
    elif page == "Register":
        register_page()
    elif page == "Login":
        login_page()
    elif page == "Dashboard":
        dashboard_page()

# Register page
def register_page():
    st.header("Register")
    st.write(register_html, unsafe_allow_html=True)

# Login page
def login_page():
    st.header("Login")
    st.write(login_html, unsafe_allow_html=True)

# Dashboard page
def dashboard_page():
    if 'user' not in st.session_state:
        st.warning("Please log in first!")
        st.experimental_rerun()
    else:
        st.header("Dashboard")
        st.write(dashboard_html, unsafe_allow_html=True)

# Load HTML content
login_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Courier Management System</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

        .login-form {
            position: relative;
            min-height: 100vh;
            z-index: 0;
            background: #4e34b6;
            padding: 30px;
            justify-content: center;
            display: grid;
            font-family: 'Poppins', sans-serif;
            grid-template-rows: 1fr auto 1fr;
            align-items: center;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        .login-form h1 {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 400;
            color: #fff;
            font-family: 'Poppins', sans-serif;
        }

        .login-form h2 {
            line-height: 40px;
            margin-bottom: 5px;
            font-size: 30px;
            font-weight: 500;
            color: #272346;
            text-align: center;
        }

        .login-form .main {
            position: relative;
            display: flex;
            margin: 30px 0;
        }

        .content {
            flex-basis: 50%;
            padding: 3em 3em;
            background: #fff;
            box-shadow: 2px 9px 49px -17px rgba(0, 0, 0, 0.1);
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
        }

        .form-img {
            flex-basis: 50%;
            background: #dfe5ea;
            background-size: cover;
            padding: 40px;
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
            align-items: center;
            display: grid;
        }

        .form-img img {
            max-width: 100%;
        }

        p {
            color: #666;
            font-size: 16px;
            line-height: 25px;
            opacity: 0.6;
            text-align: center;
        }

        .btn, button, input {
            border-radius: 35px;
        }

        .btn:hover, button:hover {
            color: #272346;
            transition: 0.5s ease;
        }

        a {
            text-decoration: none;
        }

        .login-form form {
            margin: 30px 0;
        }

        .login-form input {
            outline: none;
            margin-bottom: 15px;
            font-stretch: 16px;
            color: #999;
            text-align: left;
            padding: 14px 20px;
            width: 100%;
            display: inline-block;
            box-sizing: border-box;
            border: none;
            background: #f7fafc;
            transition: 0.3s ease;
        }

        .login-form input:focus {
            background: transparent;
            border: 1px solid #4e34b6;
        }

        .login-form button {
            font-size: 18px;
            color: #fff;
            width: 100%;
            background: #4e34b6;
            border: none;
            padding: 14px 15px;
            font-weight: 600;
            transition: 0.3s ease;
        }

        p.account a {
            color: #4e34b6;
        }

        p.account a:hover {
            text-decoration: underline;
        }

        @media (max-width: 736px) {
            .login-form .main {
                flex-direction: column;
            }

            .login-form form {
                margin-top: 30px;
                margin-bottom: 10px;
            }

            .form-img {
                border-radius: 0;
                border-bottom-left-radius: 8px;
                border-bottom-right-radius: 8px;
                order: 2;
            }

            .content {
                order: 1;
                border-radius: 0;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }
        }
    </style>
</head>
<body>
    <div class="login-form">
        <h1>Courier Management System</h1>
        <div class="container">
            <div class="main">
                <div class="content">
                    <h2>Log In</h2>
                    <form action="#" method="post">
                        <input type="text" name="" placeholder="User Name" required autofocus="">
                        <input type="password" name="" placeholder="User Password" required autofocus="">
                        <button class="btn" type="submit">Login</button>
                    </form>
                    <p class="account">Don't Have An Account? <a href="register.html">Register</a></p>
                </div>
                <div class="form-img">
                    <img src="bg.png" alt="">
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

register_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Courier Management System - Register</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }
        .register-form {
            position: relative;
            min-height: 100vh;
            z-index: 0;
            background: #4e34b6;
            padding: 30px;
            justify-content: center;
            display: grid;
            font-family: 'Poppins', sans-serif;
            grid-template-rows: 1fr auto 1fr;
            align-items: center;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        .register-form h1 {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 400;
            color: #fff;
            font-family: 'Poppins', sans-serif;
        }
        .register-form h2 {
            line-height: 40px;
            margin-bottom: 5px;
            font-size: 30px;
            font-weight: 500;
            color: #272346;
            text-align: center;
        }
        .register-form .main {
            position: relative;
            display: flex;
            margin: 30px 0;
        }
        .content {
            flex-basis: 50%;
            padding: 3em 3em;
            background: #fff;
            box-shadow: 2px 9px 49px -17px rgba(0, 0, 0, 0.1);
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
        }
        .form-img {
            flex-basis: 50%;
            background: #dfe5ea;
            background-size: cover;
            padding: 40px;
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
            align-items: center;
            display: grid;
        }
        .form-img img {
            max-width: 100%;
        }
        p {
            color: #666;
            font-size: 16px;
            line-height: 25px;
            opacity: 0.6;
            text-align: center;
        }
        .btn, button, input {
            border-radius: 35px;
        }
        .btn:hover, button:hover {
            color: #272346;
            transition: 0.5s ease;
        }
        a {
            text-decoration: none;
        }
        .register-form form {
            margin: 30px 0;
        }
        .register-form input {
            outline: none;
            margin-bottom: 15px;
            font-size: 16px;
            color: #999;
            text-align: left;
            padding: 14px 20px;
            width: 100%;
            display: inline-block;
            box-sizing: border-box;
            border: none;
            background: #f7fafc;
            transition: 0.3s ease;
        }
        .register-form input:focus {
            background: transparent;
            border: 1px solid #4e34b6;
        }
        .register-form button {
            font-size: 18px;
            color: #fff;
            width: 100%;
            background: #4e34b6;
            border: none;
            padding: 14px 15px;
            font-weight: 600;
            transition: 0.3s ease;
        }
        p.account a {
            color: #4e34b6;
        }
        p.account a:hover {
            text-decoration: underline;
        }
        @media (max-width: 736px) {
            .register-form .main {
                flex-direction: column;
            }
            .register-form form {
                margin-top: 30px;
                margin-bottom: 10px;
            }
            .form-img {
                border-radius: 0;
                border-bottom-left-radius: 8px;
                border-bottom-right-radius: 8px;
                order: 2;
            }
            .content {
                order: 1;
                border-radius: 0;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }
        }
    </style>
</head>
<body>
    <div class="register-form">
        <h1>Courier Management System</h1>
        <div class="container">
            <div class="main">
                <div class="content">
                    <h2>Register</h2>
                    <form action="#" method="post">
                        <input type="text" name="username" placeholder="User Name" required autofocus>
                        <input type="email" name="email" placeholder="Email" required>
                        <input type="password" name="password" placeholder="Password" required>
                        <input type="password" name="confirm_password" placeholder="Confirm Password" required>
                        <button class="btn" type="submit">Register</button>
                    </form>
                    <p class="account">Already Have An Account? <a href="login.html">Log In</a></p>
                </div>
                <div class="form-img">
                    <img src="bg.png" alt="Register Image">
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

dashboard_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Courier Management Dashboard</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body {
    margin: 0;
    overflow: hidden; /* Prevents scrollbars caused by background image */
}

.dashboard {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    background: rgba(0, 0, 0, 0.5); /* Optional: Adds a semi-transparent overlay */
}

.form-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.form-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.5; /* Optional: Adjusts image opacity */
}

.header {
    width: 100%;
    background: rgba(255, 255, 255, 0.8); /* Semi-transparent background for header */
    color: #4e34b6;
    padding: 20px;
    text-align: center;
    border-radius: 8px;
    margin-bottom: 20px;
    position: relative;
}

.header h1 {
    font-size: 2.5rem;
    font-weight: 600;
}

.nav {
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.user-info {
    position: relative;
}

.user-icon {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: #fff;
    border: 2px solid #4e34b6;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    overflow: hidden;
}

.user-icon img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.user-details {
    display: none;
    position: absolute;
    top: 60px; /* Adjusted to be below the icon */
    right: 0;
    background: #fff;
    color: #333;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    z-index: 10;
}

.user-details p {
    margin: 0;
    font-size: 16px;
    font-weight: 500;
}

.user-details button {
    background: #4e34b6;
    color: #fff;
    border: none;
    padding: 10px 15px;
    border-radius: 25px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: 0.3s ease;
    margin-top: 10px;
}

.user-details button:hover {
    background: #3d2a9e;
}

.logout-link {
    color: #4e34b6;
    text-decoration: none;
    font-weight: 500;
}

.logout-link:hover {
    text-decoration: underline;
}

.container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    width: 100%;
    max-width: 1200px;
}

.box {
    background: rgba(255, 255, 255, 0.9); /* Slightly transparent background for readability */
    color: #333;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    position: relative;
}

.box h2 {
    font-size: 1.8rem;
    margin-bottom: 10px;
}

.box p {
    font-size: 1rem;
    color: #666;
}

.btn {
    background: #4e34b6;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: 0.3s ease;
    margin-top: 15px;
}

.btn:hover {
    background: #3d2a9e;
}

@media (max-width: 768px) {
    .container {
        grid-template-columns: 1fr;
    }
}

    </style>
</head>
<body>
    <div class="dashboard">
        <div class="form-img">
            <img src="Blog-119-2.jpg" alt="Background Image">
        </div>
        <header class="header">
            <h1>Courier Management Dashboard</h1>
            <nav class="nav">
                <div class="user-info">
                    <div class="user-icon" id="userIcon">
                        <img src="icon.png" alt="User Icon">
                    </div>
                    <div class="user-details" id="userDetails">
                        <p id="username">Username</p>
                        <button class="btn" id="closeDetails">Close</button>
                    </div>
                </div>
                <a href="logout.html" class="logout-link">Logout</a>
            </nav>
        </header>
        <div class="container">
            <div class="box my-parcels">
                <h2>My Parcels</h2>
                <p>Track and manage all your parcels.</p>
                <button class="btn">View Parcels</button>
            </div>
            <div class="box my-agents">
                <h2>My Agents</h2>
                <p>View and manage your delivery agents.</p>
                <button class="btn">Manage Agents</button>
            </div>
            <div class="box customer-service">
                <h2>Service</h2>
                <p>Provide support and manage customer inquiries.</p>
                <button class="btn">Contact Support</button>
            </div>
            <div class="box my-status">
                <h2>My Status</h2>
                <p>Check the status of your ongoing operations.</p>
                <button class="btn">View Status</button>
            </div>
        </div>
    </div>
    <script>
        document.getElementById('userIcon').addEventListener('click', function() {
            document.getElementById('userDetails').style.display = 'block';
        });

        document.getElementById('closeDetails').addEventListener('click', function() {
            document.getElementById('userDetails').style.display = 'none';
        });
    </script>
</body>
</html>
"""

# Main function
def main():
    home_page()

if __name__ == "__main__":
    main()
