# Markdown Tips

I'm not intending this to be a "How to Use Markdown" document but rather a "Here are some cool things I learned how to do in markdown".
## Linking to local files

Typically, linking to a local file is done with:
```md
[Displayed Text](./link/to/file)
```

But sometimes, there are spaces in file names or paths. Typically, I just try to not use spaces but in the case that there are, I would use:
```md
[Displayed Text](./link%20to%20file)
```

The better way to do this is:
```md
[Displayed Text](<./link to file>)
```

Lastly, if you are trying to link to a header in another file (header not required), the link can be formatted as
```md
[[note#header|Display text]]
```
## Writing Math in Markdown using LaTeX

LaTeX can be used in markdown for math equations be encompassing the LaTeX with `$$`. For example, the quadratic formula:
```latex
$$\frac{-b \pm \sqrt{b^2-4ac}}{2a}$$
```

This would appear as:

$$\frac{-b \pm \sqrt{b^2-4ac}}{2a}$$
