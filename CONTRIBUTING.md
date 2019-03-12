# Contributing

Contributions from lab members **are welcome**!

Please open an issue or pull request for any contributions.
Pull requests will be reviewed by a maintainer, then will be merged after receiving an approval.

## Things to contribute

### Publications
We want to maintain a list of publications by lab members to major conferences and journals.
Please open a pull request to add publications that we might be missing!

Publications are sorted into separate yaml files by year in `_data/publications`.
The template for adding new publications is:
```yaml
- id: [short name (i.e. smith1992sparsity)]
  title: [publication title]
  authors: [First Last, First Last, and First Last]
  conference: [conference/journal long name]
  pdf: [https://link.to/pdf]
```

### Lab Member and Alumnus Info
We would like to keep track of current lab members and alumni.
Please open a pull request to add lab members or alumni that are not already on the list.

The list is kept in `_data/people.yml`, please make sure new additions are **sorted by last name**.
The template for adding new people:
```yaml
- name: [First Last]
  status: [msc, phd, postdoc, faculty, research associate, current title]
  website: [(optional) https://example.com]
  alumni: [(optional) msc, phd, research associate]
  year: [(optional) graduation year]
```

### Website Text
Feel free to open a PR or create an issue discussing changes to text on the website.
The website text can be found in the markdown (`*.md`) files in the root-level directory.

## Running locally
This website is built using jekyll.
To run locally, check out [this article](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll) from github pages.
