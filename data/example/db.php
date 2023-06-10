<?php
// Database configuration
$host = 'localhost';
$database = 'example';
$username = 'admin';
$password = 'asdf1234';

// Create a connection to the database
$conn = new mysqli($host, $username, $password, $database);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Connection successful
echo "Connected to the database successfully.";

// Close the connection
$conn->close();
?>