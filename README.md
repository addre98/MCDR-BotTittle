# BotTittle

通过原版 `/team` 机制，自动为地毯端假人玩家添加自定义称号前缀。

## 依赖

- MCDReforged >= 2.0.0
- `/team` 命令（原版支持）

## 工作原理

监听玩家加入事件，通过正则表达式匹配假人登录消息，自动将其加入队伍应用队伍前缀。

## 配置

首次加载后会在 `config/bot_tittle/config.json` 生成配置文件：

```json
{
    "title_prefix": "§f[§aBot§f]"
}
```
- `title_prefix`：称号前缀字符串，使用格式化代码 `§` 

## 许可

GPL-3.0
