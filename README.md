# Making a package to get an Rmd template

Hanneke Leegwater. June 2022

## Install templates directly in R studio

-   Open your R studio, or a specific R project with renv.

-   Install the templates using:

`remotes::install_github("hleegwater/RMarkdownTemplateHanneke")`

## Install when you want to add your custom templates

Note that this does not work if you also work with Renv.

-   Clone repository
-   Open Rproj project
-   Click on Build, next to the Environment, History etc
-   Install
-   Restart Rstudio

## Edit a template

-   Templates can be found in skeleton folders and skeleton files within inst/rmarkdown/templates
-   Each template has its own folder
-   Edit the skeleton file, don't forget to check if the yaml file is still okay!

## Instructions on how to build the template after changing the skeleton

1.  Save everything,
2.  Click on Build, next to the Environment, History etc
3.  Install
4.  Restart Rstudio
5.  Don't forget to commit the changes and push to the remote repository if needed!

# Work in progress

We are hoping to add a quarto template soon!

# References

This package is based on many books, searches and google hits. Especially:

-   I created a package using the instructions on <https://rstudio4edu.github.io/rstudio4edu-book/rmd-templates.html> part 12.

-   I followed the instructions on <https://rstudio4edu.github.io/rstudio4edu-book/rmd-templates.html> to create a template that I like.

-   To get todays date in the knitted html file: <https://stackoverflow.com/questions/71173343/dynamically-naming-the-output-file-in-a-custom-r-markdown-function/71174669#71174669>

-   Hopefully <https://stackoverflow.com/questions/77484159/how-to-dynamically-set-html-filename-when-rendering-quarto-documents-in-r>

And thanks to [\@burgerga](https://www.github.com/burgerga) for the official DDS2 template!
