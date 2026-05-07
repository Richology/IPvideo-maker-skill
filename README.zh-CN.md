# IP Video Maker Skill 中文版

一个面向自媒体创作者的 Codex Skill，用来把文章、脚本、截图、参考视频，转成一套可复用的短视频生产工作流。

它适合公众号作者、知识博主、独立开发者、教育内容创作者、个人 IP 创作者。目标不是写一个“一次性提示词”，而是沉淀一条可以反复跑的内容生产流水线。

## 这个 Skill 能帮你做什么

- 把长文改写成 30-90 秒短视频口播稿。
- 生成可编辑的 `segments.json` 分镜脚本。
- 指导 Codex 搭建竖屏 HyperFrames + HTML + GSAP 动画工程。
- 渲染出 MP4 视频。
- 用 ffmpeg 合成真人头像、口播视频或音频画中画。
- 发布后根据数据复盘，生成下一版迭代方案。
- 分析参考视频的节奏和结构，但不抄袭内容。

## 工作流

```mermaid
flowchart LR
  A["文章 / 脚本 / 截图 / 参考视频"] --> B["短视频口播稿"]
  B --> C["segments.json 分镜"]
  C --> D["HyperFrames HTML 动画"]
  D --> E["MP4 渲染"]
  E --> F["真人口播 / 音频 / 头像画中画"]
  F --> G["发布"]
  G --> H["数据复盘"]
  H --> B
```

## 安装

把 `self-media-video` 目录复制到你的 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R self-media-video ~/.codex/skills/
```

然后重启 Codex，或者开启一个新会话，让 Codex 发现这个 Skill。

## 快速开始

对 Codex 说：

```text
Use $self-media-video to turn this article into a 45-second short video.
```

如果你主要用中文，也可以这样说：

```text
使用 $self-media-video，把下面这篇文章改成一条 45 秒短视频。
```

为了获得更精准的结果，最好直接粘贴完整原文，而不是只发截图：

```text
使用 $self-media-video。

这是我的文章全文：
...

请帮我生成：
1. script.md
2. segments.json
3. HyperFrames 动画工程
4. draft MP4
```

## 示例提示词

```text
使用 $self-media-video，把这篇公众号文章改成一条 60 秒小红书视频。
```

```text
使用 $self-media-video，把这篇 newsletter 改成一条 45 秒真人口播 + 动画重点的视频。
```

```text
使用 $self-media-video，分析这个参考视频的节奏和视觉结构，然后为我的主题生成原创 segments.json。
```

```text
使用 $self-media-video，复盘我发布后的视频数据，并给出下一版标题和开头 5 秒的优化方案。
```

## 推荐工具链

这个 Skill 可以只用于流程指导，但配合下面这些工具会更完整：

- [HyperFrames](https://hyperframes.heygen.com)：把 HTML 动画渲染成视频
- [GSAP](https://gsap.com)：控制动画时间线
- [ffmpeg](https://ffmpeg.org)：合成音频、口播、头像画中画
- Python 3：运行辅助脚本
- Node.js：运行 HyperFrames

如果你要拆解参考视频，也可以使用：

- [hahadu4520/videoanalyzer](https://github.com/hahadu4520/videoanalyzer)

## 内置辅助脚本

生成一个可编辑的分镜模板：

```bash
self-media-video/scripts/make_segments.py --duration 45 --count 7 --out segments.json
```

检查渲染后的视频规格：

```bash
self-media-video/scripts/probe_video.sh renders/final.mp4
```

合成右下角真人口播画中画，并使用口播视频里的声音：

```bash
self-media-video/scripts/compose_pip.sh base.mp4 talking_head.mp4 final_with_pip.mp4
```

## 典型输出文件

一次完整的视频项目通常会长这样：

```text
my-video/
  script.md
  segments.json
  index.html
  assets/
    source-screenshot.png
    talking_head.mp4
  renders/
    draft.mp4
    final_with_pip.mp4
```

## 发布后复盘数据模板

视频发布后，把下面这些数据给 Codex：

```text
平台：
发布时间：
标题：
封面文案：
视频时长：
播放量：
3 秒留存：
完播率：
平均观看时长：
点赞：
收藏：
评论：
转发：
涨粉：
观众评论：
```

Codex 会判断主要瓶颈在哪里：开头钩子、标题封面、节奏、表达清晰度、视觉密度、CTA，还是分发问题。

## 仓库结构

```text
self-media-video/
  SKILL.md
  agents/
    openai.yaml
  references/
    article-to-video.md
    hyperframes.md
    publish-review.md
    reference-video-analysis.md
  scripts/
    make_segments.py
    probe_video.sh
    compose_pip.sh
```

## 重要说明

- 直接粘贴原文，比从截图 OCR 更准确。
- 参考视频应该用来学习节奏和结构，不应该照搬内容。
- 第一版渲染永远只是草稿，发布前要检查关键帧截图。
- 加入真人口播、头像或声音，通常会让视频更像可发布作品。

## License

MIT

