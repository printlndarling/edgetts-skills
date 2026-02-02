# TTS Service API Reference

## Available Voices

### Chinese Voices (Multilingual)

#### zh-CN-XiaoxiaoMultilingualNeural (Default)
- **Language**: Chinese (Mandarin, Simplified) + English
- **Gender**: Female
- **Description**: Natural, warm, versatile voice suitable for various content
- **Best for**: General narration, audiobooks, conversational content

#### zh-CN-XiaoyiMultilingualNeural
- **Language**: Chinese (Mandarin, Simplified) + English
- **Gender**: Female
- **Description**: Clear, professional tone
- **Best for**: Business content, presentations

#### zh-CN-YunjianMultilingualNeural
- **Language**: Chinese (Mandarin, Simplified) + English
- **Gender**: Male
- **Description**: Deep, authoritative voice
- **Best for**: Documentary narration, professional content

#### zh-CN-YunxiMultilingualNeural
- **Language**: Chinese (Mandarin, Simplified) + English
- **Gender**: Male
- **Description**: Young, energetic tone
- **Best for**: Casual content, marketing

#### zh-CN-YunyangMultilingualNeural
- **Language**: Chinese (Mandarin, Simplified) + English
- **Gender**: Male
- **Description**: Professional news anchor style
- **Best for**: News broadcasts, formal announcements

### English Voices

#### en-US-AvaMultilingualNeural
- **Language**: English (US) + Multiple languages
- **Gender**: Female
- **Description**: Clear American accent
- **Best for**: International content

#### en-US-AndrewMultilingualNeural
- **Language**: English (US) + Multiple languages
- **Gender**: Male
- **Description**: Confident, professional
- **Best for**: Business presentations

#### en-US-EmmaMultilingualNeural
- **Language**: English (US) + Multiple languages
- **Gender**: Female
- **Description**: Warm, friendly
- **Best for**: Customer service, tutorials

#### en-US-BrianMultilingualNeural
- **Language**: English (US) + Multiple languages
- **Gender**: Male
- **Description**: Casual, approachable
- **Best for**: Conversational content

### Regional Chinese Voices

#### zh-HK-HiuMaanNeural
- **Language**: Cantonese (Hong Kong)
- **Gender**: Female

#### zh-HK-WanLungNeural
- **Language**: Cantonese (Hong Kong)
- **Gender**: Male

#### zh-TW-HsiaoChenNeural
- **Language**: Taiwanese Mandarin
- **Gender**: Female

#### zh-TW-YunJheNeural
- **Language**: Taiwanese Mandarin
- **Gender**: Male

## Voice Styles

Available styles depend on the voice. Common styles include:

- `general` - Default neutral style
- `chat` - Casual conversational
- `customerservice` - Professional and helpful
- `newscast` - News anchor delivery
- `newscast-casual` - Relaxed news style
- `newscast-formal` - Formal news style
- `cheerful` - Upbeat and positive
- `empathetic` - Warm and understanding
- `angry` - Emotional intensity
- `sad` - Melancholic tone
- `excited` - High energy
- `friendly` - Approachable warmth
- `terrified` - Fear expression
- `shouting` - Loud emphasis
- `whispering` - Soft and intimate
- `hopeful` - Optimistic tone

**Note**: Not all voices support all styles. Check Microsoft's documentation for voice-specific style support.

## Voice Roles

Role adaptation allows voices to simulate different age groups or personas:

- `YoungAdultFemale` - Young woman
- `YoungAdultMale` - Young man
- `OlderAdultFemale` - Mature woman
- `OlderAdultMale` - Mature man
- `SeniorFemale` - Elderly woman
- `SeniorMale` - Elderly man
- `Girl` - Young girl
- `Boy` - Young boy

## Audio Formats

### Supported Formats

- `mp3` (default) - Widely compatible, good compression
- `opus` - High quality, efficient for streaming
- `aac` - Apple-optimized format
- `flac` - Lossless audio quality
- `wav` - Uncompressed PCM audio
- `pcm` - Raw PCM data

### Format Selection Guide

- **General use**: mp3 (best compatibility)
- **High quality**: flac or wav
- **Streaming**: opus
- **iOS/Apple**: aac
- **Processing**: wav or pcm

## Parameter Details

### Speed (0.25 - 2.0)
- `0.25` - Very slow (75% slower)
- `0.5` - Half speed (50% slower)
- `0.75` - Slightly slow (25% slower)
- `1.0` - Normal speed (default)
- `1.25` - Slightly fast (25% faster)
- `1.5` - Fast (50% faster)
- `2.0` - Very fast (100% faster)

**Recommendation**: Stay between 0.8-1.5 for natural sound

### Pitch (0.5 - 1.5)
- `0.5` - Very low pitch (-50%)
- `0.75` - Slightly low pitch (-25%)
- `1.0` - Normal pitch (default)
- `1.25` - Slightly high pitch (+25%)
- `1.5` - Very high pitch (+50%)

**Recommendation**: Stay between 0.9-1.2 for natural sound

### Style Degree (0.01 - 2.0)
Controls the intensity of the selected style:
- `0.01` - Minimal style influence
- `0.5` - Subtle style application
- `1.0` - Default style intensity
- `1.5` - Pronounced style
- `2.0` - Maximum style intensity

## Text Cleaning Options

### remove_markdown
Removes Markdown formatting:
- `**bold**` → bold
- `*italic*` → italic
- `# Header` → Header
- `[link](url)` → link

### remove_emoji
Removes all emoji characters:
- `Hello 😊` → Hello
- `Great! 🎉` → Great!

### remove_urls
Removes HTTP/HTTPS URLs:
- `Visit https://example.com` → Visit
- `Check http://site.com for info` → Check for info

### remove_line_breaks
Removes newline characters:
- Preserves sentence flow
- Useful for continuous narration

### remove_citation_numbers
Removes citation brackets:
- `According to research[1]` → According to research
- `The study shows[2][3]` → The study shows

### custom_keywords
Comma-separated list of words to remove:
- `custom_keywords: "um,uh,like"` removes filler words
- Case-insensitive matching

## Complete Request Example

```python
import requests

response = requests.post(
    'https://tts.4321024.xyz/v1/audio/speech',
    headers={
        'Authorization': 'Bearer 123321',
        'Content-Type': 'application/json'
    },
    json={
        # Required parameters
        'model': 'tts-1',
        'voice': 'zh-CN-XiaoxiaoMultilingualNeural',
        'input': 'Hello world! This is a test.',
        
        # Optional basic parameters
        'speed': 1.2,
        'pitch': 1.0,
        'response_format': 'mp3',
        'stream': False,
        
        # Advanced voice parameters
        'style': 'cheerful',
        'role': 'YoungAdultFemale',
        'styleDegree': 1.3,
        
        # Text cleaning options
        'cleaning_options': {
            'remove_markdown': True,
            'remove_emoji': True,
            'remove_urls': True,
            'remove_line_breaks': False,
            'remove_citation_numbers': True,
            'custom_keywords': 'um,uh,like'
        }
    }
)

if response.status_code == 200:
    with open('output.mp3', 'wb') as f:
        f.write(response.content)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

## Rate Limits and Quotas

- **Character limit**: ~120,000 characters per request
- **Concurrent requests**: Limited by Cloudflare Workers
- **Rate limiting**: May apply based on usage
- **First request**: May have 1-2 minute initialization delay

## Best Practices

1. **Text length**: For texts over 50,000 characters, use streaming mode
2. **Error handling**: Always check response status codes
3. **Voice selection**: Test multiple voices to find the best fit
4. **Speed/pitch**: Use subtle adjustments (0.9-1.2 range)
5. **Text cleaning**: Enable appropriate cleaning options for your content
6. **Caching**: Cache generated audio for repeated content
7. **Testing**: Test with sample text before processing large batches
