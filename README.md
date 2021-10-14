# SomeScripts
一些个人使用脚本

### `install.sh`

加速安装 `ohmyzsh` (前提是安装了`zsh`)

> 可能需要的字体
>
> https://github.com/powerline/fonts

#### Win10+

可以使用 `Git Bash` 安装路径下解压 `zsh-5.8-5-x86_64.pkg.tar`



当然也可以使用官方的安装方式

https://github.com/ohmyzsh/ohmyzsh#basic-installation

### `fail2ban.sh`

最简单的防止SSH暴力破解的脚本

https://github.com/EricSUID/Fail2ban

### `uPing`

24小时监测VPS延迟

https://github.com/EricSUID/uPing

### `bensh.sh`

Linux服务器测试脚本

https://github.com/EricSUID/bench.sh-Others

### `V2.sh`

> V2RAY 基于 NGINX 的 VMESS+WS+TLS+Website(Use Host)+Rinetd BBR 一键安装脚本

手动更新V2ray内核的的命令行

- wget https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh

- chmod +x install-release.sh

- bash install-release.sh --version ${版本号} -f


### `Auto sign-in ld246.py`

> 链滴(ld246.com) 的自动登录脚本

脚本依赖于 `Python` + `Selenium` + `ChromeDriver`, 测试环境为 Win 10

- `pip install selenium` 命令安装 `selenium`

- `pip install win10toast` 命令安装 `win10 桌面消息通知`

- 下载对应的 [Chrome 浏览器驱动](http://npm.taobao.org/mirrors/chromedriver/), 注意驱动版本号要与浏览器版本号一致

- 解压驱动压缩包，将解压后的 `.exe` 文件移动到 `Python 安装目录` 下的 `scripts` 文件夹中
