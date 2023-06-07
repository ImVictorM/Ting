# Ting 🌐

## Project Context 💡
This project simulates a document indexing algorithm similar to Google's, capable of identifying occurrences of terms in text files.

The  program has two main modules:
- <strong>File management module</strong>: (`/ting_file_management`) that allows you to attach text files (.txt);
- <strong>Search module</strong>: (`/ting_word_searches`) that allows operating search functions on attached files.

### Acquired Knowledge :book:
In this project, I was able to:
- Manipulate and create Queues;
- Manipulate text files.

## Main Technologies 🧰
<table>
    <thead>
        <tr>
            <th>Python</th>
            <th>Pytest</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
               <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" 
                       alt="python" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
            <td align="center">
                <a href="https://docs.pytest.org/en/7.3.x/" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/200px-Pytest_logo.svg.png" 
                       alt="pytest" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
        </tr>
    </tbody>
</table>

## Running the application ⚙️

1. Clone the repository and enter it
```
git clone git@github.com:ImVictorM/Ting.git && cd Ting
```
2. Create the virtual environment
```
python3 -m venv .venv && source .venv/bin/activate
```
3. Install the dependencies
```
python3 -m pip install -r dev-requirements.txt
```

## Testing 🛠️
To run all tests:
```
python3 -m pytest
```
Running only one test file:
```
python3 -m pytest {test_file_path}.py
```
