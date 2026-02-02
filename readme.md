---
name: tts-service
description: Text-to-speech service that converts text to natural-sounding audio files using Microsoft Edge TTS. Use when users request to convert text to speech, generate audio from text, create voice narration, produce audiobooks, or need TTS/audio generation functionality. Supports Chinese and English with high-quality neural voices.
---

# TTS Service

Convert text to natural-sounding speech using Microsoft Edge TTS via OpenAI-compatible API.

## Quick Start

Basic TTS generation:

```python
import requests

response = requests.post(
    'https://tts.4321024.xyz/v1/audio/speech',
    headers={
        'Authorization': 'Bearer 123321',
        'Content-Type': 'application/json'
    },
    json={
        'model': 'tts-1',
        'voice': 'zh-CN-XiaoxiaoMultilingualNeural',
        'input': 'Your text here'
    }
)

with open('output.mp3', 'wb') as f:
    f.write(response.content)
```

## Core Parameters

### Required
- `input` (string): Text to convert (up to ~120,000 characters)
- `model` (string): Use `"tts-1"` or `"tts-1-hd"`
- `voice` (string): Voice identifier (see Voice Selection below)

### Optional
- `speed` (float): 0.25-2.0, default 1.0
- `pitch` (float): 0.5-1.5, default 1.0  
- `stream` (boolean): Enable streaming mode, default false
- `response_format` (string): "mp3" (default), "opus", "aac", "flac", "wav", "pcm"

### Advanced Options
- `style` (string): Voice style (general, chat, newscast, etc.)
- `role` (string): Role adaptation (YoungAdultFemale, etc.)
- `styleDegree` (float): 0.01-2.0, style intensity

## Voice Selection

**Default voice**: `zh-CN-XiaoxiaoMultilingualNeural` (Chinese female, supports English)

**OpenAI-compatible aliases**:
- `shimmer` → Gentle female
- `alloy` → Professional male
- `fable` → Energetic male
- `onyx` → Lively female
- `nova` → Cheerful male
- `echo` → Northeastern Chinese female

For complete voice list and characteristics, see [Voice Reference](references/api_reference.md).

## Text Processing

The service automatically cleans text before synthesis:

```python
# Customize cleaning with cleaning_options
{
    'remove_markdown': True,      # Remove **bold**, *italic*
    'remove_emoji': True,          # Remove 😊 emoji
    'remove_urls': True,           # Remove http://...
    'remove_line_breaks': False,   # Keep \n breaks
    'remove_citation_numbers': True,  # Remove [1], [2]
    'custom_keywords': 'word1,word2'  # Remove specific words
}
```

## Common Workflows

### Generate Simple Audio

```python
response = requests.post(
    'https://tts.4321024.xyz/v1/audio/speech',
    headers={'Authorization': 'Bearer 123321'},
    json={
        'model': 'tts-1',
        'voice': 'zh-CN-XiaoxiaoMultilingualNeural',
        'input': 'Hello world! 你好世界!'
    }
)
```

### Streaming for Long Text

```python
response = requests.post(
    'https://tts.4321024.xyz/v1/audio/speech',
    headers={'Authorization': 'Bearer 123321'},
    json={
        'model': 'tts-1',
        'voice': 'zh-CN-XiaoxiaoMultilingualNeural',
        'input': 'Very long text...',
        'stream': True
    },
    stream=True
)

with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

### Adjust Speed and Pitch

```python
json_data = {
    'model': 'tts-1',
    'voice': 'zh-CN-XiaoxiaoMultilingualNeural',
    'input': 'Faster speech with higher pitch',
    'speed': 1.3,
    'pitch': 1.2
}
```

### Custom Voice Style

```python
json_data = {
    'model': 'tts-1',
    'voice': 'zh-CN-XiaoxiaoMultilingualNeural',
    'input': 'News broadcast style',
    'style': 'newscast',
    'styleDegree': 1.5
}
```

## Error Handling

Always check response status:

```python
if response.status_code == 200:
    with open('output.mp3', 'wb') as f:
        f.write(response.content)
else:
    print(f"Error: {response.status_code}")
    print(response.json())
```

Common errors:
- 401: Invalid API key
- 400: Invalid parameters or text too long
- 429: Rate limit exceeded

## Limitations

- Maximum text length: ~120,000 characters per request
- Rate limits apply (Cloudflare Workers limits)
- First request may have initialization delay (1-2 minutes)
