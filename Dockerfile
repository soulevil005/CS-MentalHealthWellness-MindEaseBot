# Base Rasa image
FROM rasa/rasa:3.6.2

# Copy project files
COPY . /app

# Set working directory
WORKDIR /app

# Expose Rasa server port
EXPOSE 5005

# Run the main Rasa server
CMD ["run", "--enable-api", "--cors", "*"]
