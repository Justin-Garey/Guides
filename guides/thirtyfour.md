# Word of the Day Webscraper in Rust with thirtyfour

## Setup

To start our rust project, run ```cargo new thirtyfour-primer```. 

```cd``` into the newly created project and start by modifying the **Cargo.toml**. These dependencies need added.
```
[dependencies]
tokio = { version = "1.32.0", features = ["full"] }
thirtyfour = "0.31.0"
```
- You can also use ```cargo add package``` to add these to your project.
- **tokio** gives the asynchronous abilities needed for our scraper.
- **thirtyfour** is the selenium like library that is able to use a webdriver to interact with the page.

Before anything can be operated, the chromedriver needs to be installed. Chromedriver versions can be found [here](https://chromedriver.chromium.org/downloads/version-selection) but if the version needed is newer, then look [here](https://googlechromelabs.github.io/chrome-for-testing/). The chromedriver version you need is the version of chrome you have installed on your system.

Unzip the chromedriver zip file once downloaded. Now the chromedriver is ready to go.

## Programming our Webscraper

All code will take place in main.rs.

We start by importing the thirtyfour library.
```
use thirtyfour::prelude::*;
```

Then we can create the body of our main function. Since we are using the webdriver, it needs to be made into an asynchronous function and return a webdriver result. Using the tokio::main macro, we can do just that.
```
#[tokio::main]
async fn main() -> WebDriverResult<()> {

    Ok(())
}
```

Now the webdriver can be instantiated.
```
let driver = WebDriver::new("http://localhost:9515", DesiredCapabilities::chrome()).await?;
```
- The webdriver takes in a port it can live on and the capabilities it should have. Here, the base is used.
- There is an await method attached to this so the code does not move on until the webdriver is up.

Time to go to a website! In this example, we will go to the Merriam Webster dictionary for their word of the day.
```
driver.goto("https://www.merriam-webster.com/word-of-the-day").await?;
```
- We give the driver a location and wait for it to complete.

Once on a website, we want to do something. Start by finding an element.
```
let word_elem = driver.find(By::ClassName("word-header-txt")).await?;
```
- We create a variable to hold our webelement called word_elem.
- Then we use the driver to find our element by classname.
  - The classname of an element can be found by inspecting on the target webpage (right click and the inspect option should appear). Then using the select tool (in the very top left of the inspect window there is a small icon with a dashed window and pointer arrow) or using ctrl+shift+c, click on the element you want to view the details of. The location in the html of the element will be highlighted in the inspect window, then if there is a classname it will be seen. For our Merriam Webster example, this process will highlight ```<h2 class="word-header-txt">skulk</h2>```. The class attribute is what we use for ClassName.

In case internet is slow, we can wait for the element to be displayed before acting on it.
```
word_elem.wait_until().displayed().await?;
```

Then we can extract the contents of our element by using the ```.text()``` method
```
let merriam_webster_word = word_elem.text().await?;
```

Now we can start on grabbing the definition in a similar fashion to how the word was retrieved.
```
let definition_elem = driver.find(By::ClassName("wod-definition-container")).await?;
```
- Because the definition itself does not have any unique properties, we can build our way there. This grabs the container that holds the definition so there is still one more step.

To finally get the definition, we will use By::Tag
```
let definition_p = definition_elem.find(By::Tag("p")).await?;
```
- The first **p** tag in the container is our definition, so we just yank that out of the element.

Finally we can grab the text of the definition and print out our results.
```
let merriam_webster_definition = definition_p.text().await?;
println!("\nMerriam Webster");
println!("{}", merriam_webster_word);
println!("{}", merriam_webster_definition);
```

## The resulting program
```
use thirtyfour::prelude::*;

#[tokio::main]
async fn main() -> WebDriverResult<()> {
    let driver = WebDriver::new("http://localhost:9515", DesiredCapabilities::chrome()).await?;

    driver
        .goto("https://www.merriam-webster.com/word-of-the-day")
        .await?;
    let word_elem = driver.find(By::ClassName("word-header-txt")).await?;
    word_elem.wait_until().displayed().await?;
    let merriam_webster_word = word_elem.text().await?;

    let definition_elem = driver
        .find(By::ClassName("wod-definition-container"))
        .await?;
    let definition_p = definition_elem.find(By::Tag("p")).await?;
    let merriam_webster_definition = definition_p.text().await?;
    
    println!("\nMerriam Webster");
    println!("{}", merriam_webster_word);
    println!("{}", merriam_webster_definition);

    driver.quit().await?;

    Ok(())
}
```

## Running the Program

Start by running the chromedriver executable.

While the chromedriver is up, use ```cargo run``` to start the program.

## Expected Output

When the program runs, you will see the chromedriver pop up to the webpage. After the program has extracted the desired information, the webdriver will close. In the console, you should see the word of the day followed by its definition.
```
Merriam Webster
skulk
To skulk is to move around or hide in a stealthy or secretive way. A person or animal that is said to be skulking is often assumed or considered to be up to some form of wrongdoing or mischief.
```

## Errors & Solutions
```
Error: NewSessionError(Failed(hyper::Error(Connect, ConnectError("tcp connect error", Os { code: 111, kind: ConnectionRefused, message: "Connection refused" }))))
```
- Chromedriver is not running

```
Error: NewSessionError(NotW3C(Object {"error": String("unknown error"), "message": String("unknown error: cannot find Chrome binary"), "stacktrace": String("")}))
```
- Google Chrome is not installed

```
Error: NewSessionError(SessionNotCreated(WebDriver { error: SessionNotCreated, message: "session not created: This version of ChromeDriver only supports Chrome version 114\nCurrent browser version is 118.0.5993.117 with binary path /usr/bin/google-chrome", stacktrace: "" }))
```
- The incorrect version of the chromedriver is installed

## References

- https://itehax.com/blog/web-scraping-using-rust

- https://github.com/itehax/rust-scraping/tree/master

- https://docs.rs/thirtyfour/latest/thirtyfour/

- https://github.com/stevepryde/thirtyfour