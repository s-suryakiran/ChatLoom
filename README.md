# ChatLoom

ChatLoom is a specialized chatbot that leverages OpenAI's powerful language models to answer questions specifically related to the cosmos and astrophysics. Dive into the mysteries of the universe with accurate and comprehensive responses!

## Features:
- **Specialized Knowledge**: Focuses primarily on cosmos and astrophysics.
- **Powered by OpenAI**: Utilizes the latest OpenAI models to provide reliable and detailed answers.
- **Easy Setup**: With just a few steps, you can have ChatLoom running on your local system.

## Installation & Setup:

1. **Clone the Repository**:
   ```bash
   git clone [URL of your repository]
   ```

2. **Navigate to the Cloned Directory**:
   ```bash
   cd path_to_directory
   ```
3. **Create a New Virtual Environment (Optional but Recommended)**:
   - For virtualenv:
     ```bash
     virtualenv venv
     source venv/bin/activate  # On Windows use: venv\Scripts\activate
     ```
   - For conda:
     ```bash
     conda create --name chatloom_env python=3.8
     conda activate chatloom_env
     ```

4. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Setting up Environment Variables**:
   - Rename the `.env_sample` file to `.env`.
   - Open the newly named `.env` file in any text editor of your choice.
   - Locate the placeholder for the OpenAI API key and replace it with your actual key.

## Usage:

After completing the above steps, run the following in Terminal: 
  ```bash
  chainlit run main.py -w
  ```


