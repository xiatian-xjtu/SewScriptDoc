# Summer-Docs

Documentation for Summer Studio

Built with [Sphinx](https://www.sphinx-doc.org/),  and host on [Read the Docs](https://readthedocs.org/)

## Build guide

### Setup

- 安装Python
- 安装Git

**Step 1.** 克隆本仓库并创建虚拟环境(非必须, 但是建议)

[Installing packages using pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

```bash
$ git clone https://github.com/mbedmicro/DAPLink
$ cd summer-docs
$ py -m venv env
```


### Activate virtual environment

**Step 2.** 激活虚拟环境, 并安装必要的包.

```bash
$ .\env\Scripts\activate
$ py -m pip install -r requirements.txt
```

### Render the documentation as HTML

**Step 3.** 输出本地html, 打开 `docs/build/html/index.html` 查看

```bash
$ cd docs
$ make clean // 不是必须
$ make html  
```




## Reference

[多语言](https://docs.readthedocs.io/en/stable/localization.html#projects-with-multiple-translations-sphinx-only)

[reStructuredText语法参考](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)

