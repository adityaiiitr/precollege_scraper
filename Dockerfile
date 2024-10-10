# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

# Expose the port the app runs on
EXPOSE 8000

# Run the command to start the FastAPI server
CMD ["python", "main.py"]
