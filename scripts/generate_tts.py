#!/usr/bin/env python3
"""
TTS Service Generator Script

Quick script to generate speech from text using the TTS service.
"""

import requests
import sys
from pathlib import Path

# Service configuration
API_URL = "https://tts.4321024.xyz/v1/audio/speech"
API_KEY = "123321"
DEFAULT_VOICE = "zh-CN-XiaoxiaoMultilingualNeural"


def generate_speech(
    text,
    output_file="output.mp3",
    voice=DEFAULT_VOICE,
    speed=1.0,
    pitch=1.0,
    stream=False,
    response_format="mp3"
):
    """
    Generate speech from text.
    
    Args:
        text: Text to convert to speech
        output_file: Output audio file path
        voice: Voice identifier
        speed: Speech speed (0.25-2.0)
        pitch: Voice pitch (0.5-1.5)
        stream: Enable streaming mode
        response_format: Audio format (mp3, opus, aac, flac, wav, pcm)
    
    Returns:
        True if successful, False otherwise
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "tts-1",
        "voice": voice,
        "input": text,
        "speed": speed,
        "pitch": pitch,
        "stream": stream,
        "response_format": response_format
    }
    
    try:
        print(f"Generating speech...")
        print(f"Voice: {voice}")
        print(f"Speed: {speed}x, Pitch: {pitch}x")
        print(f"Text length: {len(text)} characters")
        
        if stream:
            response = requests.post(API_URL, headers=headers, json=payload, stream=True)
        else:
            response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            output_path = Path(output_file)
            
            if stream:
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
            else:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
            
            print(f"✓ Audio saved to: {output_path.absolute()}")
            return True
        else:
            print(f"✗ Error {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"✗ Exception: {e}")
        return False


def generate_from_file(input_file, output_file=None, **kwargs):
    """
    Generate speech from a text file.
    
    Args:
        input_file: Path to text file
        output_file: Output audio file (defaults to input_file.mp3)
        **kwargs: Additional arguments for generate_speech()
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"✗ File not found: {input_file}")
        return False
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if not output_file:
        output_file = input_path.with_suffix('.mp3')
    
    return generate_speech(text, output_file, **kwargs)


if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Generate from text:")
        print(f"    python {sys.argv[0]} \"Your text here\" [output.mp3]")
        print("  Generate from file:")
        print(f"    python {sys.argv[0]} --file input.txt [output.mp3]")
        print("\nExamples:")
        print(f"  python {sys.argv[0]} \"Hello world!\"")
        print(f"  python {sys.argv[0]} \"你好世界\" output.mp3")
        print(f"  python {sys.argv[0]} --file story.txt audiobook.mp3")
        sys.exit(1)
    
    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("✗ Please specify input file")
            sys.exit(1)
        input_file = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else None
        success = generate_from_file(input_file, output_file)
    else:
        text = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "output.mp3"
        success = generate_speech(text, output_file)
    
    sys.exit(0 if success else 1)
