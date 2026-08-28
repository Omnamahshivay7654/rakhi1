import os
import wave
import struct
import math

def ensure_dirs():
    os.makedirs('images', exist_ok=True)
    os.makedirs('audio', exist_ok=True)

# Generate Audio WAV Files (which work as audio src in browser audio player or can be linked)
def generate_audio_files():
    sample_rate = 44100
    duration = 10.0 # 10 seconds looping melody
    num_samples = int(sample_rate * duration)
    
    notes = [261.63, 293.66, 329.63, 392.00, 440.00, 523.25, 587.33, 659.25]
    
    with wave.open('audio/rakhi-song.mp3', 'w') as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        frames = bytearray()
        for i in range(num_samples):
            t = i / sample_rate
            note_idx = int((t * 1.6)) % len(notes)
            freq = notes[note_idx]
            
            env = 0.6 + 0.4 * math.sin(math.pi * (t * 1.6 % 1))
            val1 = math.sin(2 * math.pi * freq * t)
            val2 = 0.3 * math.sin(2 * math.pi * (freq * 2) * t)
            val3 = 0.15 * math.sin(2 * math.pi * (freq * 1.5) * t)
            
            sample_val = int((val1 + val2 + val3) * env * 10000)
            sample_val = max(-32768, min(32767, sample_val))
            
            packed = struct.pack('<h', sample_val)
            frames.extend(packed)
            frames.extend(packed)
            
        wav_file.writeframes(frames)
        
    bell_duration = 2.0
    num_bell_samples = int(sample_rate * bell_duration)
    with wave.open('audio/bell.mp3', 'w') as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        frames = bytearray()
        for i in range(num_bell_samples):
            t = i / sample_rate
            env = math.exp(-3.0 * t)
            val = (math.sin(2 * math.pi * 1200 * t) + 
                   0.5 * math.sin(2 * math.pi * 2400 * t) + 
                   0.25 * math.sin(2 * math.pi * 3600 * t))
            
            sample_val = int(val * env * 15000)
            sample_val = max(-32768, min(32767, sample_val))
            
            packed = struct.pack('<h', sample_val)
            frames.extend(packed)
            frames.extend(packed)
            
        wav_file.writeframes(frames)

SVG_BROTHER_SISTER = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="100%" height="100%">
  <defs>
    <radialGradient id="bgGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFD700" stop-opacity="0.8"/>
      <stop offset="40%" stop-color="#FF9933" stop-opacity="0.5"/>
      <stop offset="80%" stop-color="#8B0000" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#4A0E17" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE066"/>
      <stop offset="50%" stop-color="#FFD700"/>
      <stop offset="100%" stop-color="#DAA520"/>
    </linearGradient>
    <linearGradient id="sareeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E85D75"/>
      <stop offset="50%" stop-color="#8B0000"/>
      <stop offset="100%" stop-color="#4A0E17"/>
    </linearGradient>
    <linearGradient id="kurtaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFDD0"/>
      <stop offset="50%" stop-color="#FF9933"/>
      <stop offset="100%" stop-color="#CC6600"/>
    </linearGradient>
    <radialGradient id="diyaGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="30%" stop-color="#FFFF66"/>
      <stop offset="70%" stop-color="#FF9933"/>
      <stop offset="100%" stop-color="#FF0000" stop-opacity="0"/>
    </radialGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background Aura -->
  <circle cx="400" cy="400" r="380" fill="url(#bgGlow)"/>

  <!-- Outer Decorative Mandala Halo -->
  <g stroke="url(#goldGrad)" stroke-width="2" fill="none" opacity="0.6">
    <circle cx="400" cy="380" r="280" stroke-dasharray="8 6"/>
    <circle cx="400" cy="380" r="260"/>
    <circle cx="400" cy="380" r="240" stroke-dasharray="4 4"/>
    <!-- Mandala Petals -->
    <path d="M400,100 Q430,130 400,160 Q370,130 400,100 Z" fill="url(#goldGrad)" opacity="0.4"/>
    <path d="M400,660 Q430,630 400,600 Q370,630 400,660 Z" fill="url(#goldGrad)" opacity="0.4"/>
    <path d="M120,380 Q150,410 180,380 Q150,350 120,380 Z" fill="url(#goldGrad)" opacity="0.4"/>
    <path d="M680,380 Q650,410 620,380 Q650,350 680,380 Z" fill="url(#goldGrad)" opacity="0.4"/>
  </g>

  <!-- Brother Figure -->
  <g filter="url(#shadow)">
    <path d="M220,700 C220,540 270,480 320,460 C370,480 390,520 400,700 Z" fill="url(#kurtaGrad)"/>
    <path d="M310,470 L310,650 M325,470 L325,650" stroke="url(#goldGrad)" stroke-width="4"/>
    <circle cx="315" cy="400" r="50" fill="#6D4C41"/>
    <path d="M270,390 C270,340 360,340 360,390 C340,360 290,360 270,390 Z" fill="#2C1609"/>
    <path d="M230,520 Q310,580 370,510" fill="none" stroke="url(#goldGrad)" stroke-width="14" stroke-linecap="round"/>
  </g>

  <!-- Sister Figure -->
  <g filter="url(#shadow)">
    <path d="M400,700 C410,530 440,470 490,450 C550,470 590,540 600,700 Z" fill="url(#sareeGrad)"/>
    <path d="M440,465 Q510,600 580,680" fill="none" stroke="url(#goldGrad)" stroke-width="12"/>
    <circle cx="490" cy="390" r="46" fill="#8D6E63"/>
    <path d="M445,390 C445,335 535,335 535,390 C520,350 460,350 445,390 Z" fill="#1B0000"/>
    <circle cx="525" cy="370" r="10" fill="#FFFDD0"/>
    <circle cx="535" cy="385" r="10" fill="#FFFDD0"/>
    <circle cx="530" cy="400" r="10" fill="#FFFDD0"/>
    <circle cx="475" cy="385" r="4" fill="#FFD700"/>
  </g>

  <!-- Aarti Thali Held -->
  <g filter="url(#shadow)">
    <ellipse cx="400" cy="580" rx="140" ry="45" fill="url(#goldGrad)"/>
    <ellipse cx="400" cy="580" rx="125" ry="38" fill="#8B0000" opacity="0.3"/>
    <ellipse cx="400" cy="580" rx="120" ry="35" fill="url(#goldGrad)" opacity="0.6"/>
    
    <path d="M370,575 Q400,595 430,575 Q400,565 370,575 Z" fill="#DAA520"/>
    <ellipse cx="400" cy="550" rx="60" ry="60" fill="url(#diyaGlow)"/>
    <path d="M395,570 Q400,535 405,570 Z" fill="#FFD700"/>
    <path d="M397,570 Q400,545 403,570 Z" fill="#FFFFFF"/>

    <circle cx="330" cy="580" r="12" fill="#E85D75"/>
    <circle cx="345" cy="585" r="10" fill="#FF9933"/>
    <circle cx="460" cy="580" r="10" fill="#FF0000"/>
    <circle cx="475" cy="582" r="8" fill="#FFFDD0"/>
  </g>

  <!-- Floating Sparkles & Petals -->
  <g fill="url(#goldGrad)">
    <path d="M150,200 L155,215 L170,220 L155,225 L150,240 L145,225 L130,220 L145,215 Z"/>
    <path d="M650,220 L654,230 L665,234 L654,238 L650,248 L646,238 L635,234 L646,230 Z"/>
  </g>
</svg>'''

def make_rakhi_svg(name, main_color, accent_color, motif_type):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="g_{name}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE066"/>
      <stop offset="50%" stop-color="{accent_color}"/>
      <stop offset="100%" stop-color="#DAA520"/>
    </linearGradient>
    <radialGradient id="gem_{name}" cx="30%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="40%" stop-color="{main_color}"/>
      <stop offset="100%" stop-color="#2C0000"/>
    </radialGradient>
    <filter id="sh_{name}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <g stroke="url(#g_{name})" stroke-width="8" stroke-linecap="round">
    <path d="M0,250 C80,230 150,270 250,250" fill="none" stroke="{main_color}" stroke-width="6"/>
    <path d="M0,250 C80,270 150,230 250,250" fill="none" stroke="{accent_color}" stroke-width="6"/>
    <path d="M250,250 C350,230 420,270 500,250" fill="none" stroke="{main_color}" stroke-width="6"/>
    <path d="M250,250 C350,270 420,230 500,250" fill="none" stroke="{accent_color}" stroke-width="6"/>
  </g>

  <g fill="url(#g_{name})">
    <circle cx="100" cy="250" r="10"/>
    <circle cx="130" cy="250" r="7"/>
    <circle cx="155" cy="250" r="5"/>
    <circle cx="400" cy="250" r="10"/>
    <circle cx="370" cy="250" r="7"/>
    <circle cx="345" cy="250" r="5"/>
  </g>

  <g filter="url(#sh_{name})">
    <circle cx="250" cy="250" r="110" fill="url(#g_{name})"/>
    <circle cx="250" cy="250" r="95" fill="{main_color}"/>
    
    <g stroke="url(#g_{name})" stroke-width="3" fill="none">
      <circle cx="250" cy="250" r="85" stroke-dasharray="10 6"/>
      <circle cx="250" cy="250" r="70"/>
    </g>

    {motif_type}

    <circle cx="250" cy="250" r="28" fill="url(#gem_{name})"/>
    <circle cx="242" cy="242" r="7" fill="#FFFFFF" opacity="0.8"/>
  </g>
</svg>'''

RAKHI_MOTIFS = [
    '''<g fill="url(#g_rakhi1)"><polygon points="250,150 265,220 335,220 280,260 300,330 250,285 200,330 220,260 165,220 235,220"/></g>''',
    '''<g stroke="#FFD700" stroke-width="3" fill="none"><circle cx="250" cy="250" r="55"/><path d="M250,180 L250,320 M180,250 L320,250 M200,200 L300,300 M200,300 L300,200"/></g>''',
    '''<g fill="#FFFDD0"><circle cx="250" cy="185" r="12"/><circle cx="315" cy="250" r="12"/><circle cx="250" cy="315" r="12"/><circle cx="185" cy="250" r="12"/><circle cx="204" cy="204" r="10"/><circle cx="296" cy="204" r="10"/><circle cx="296" cy="296" r="10"/><circle cx="204" cy="296" r="10"/></g>''',
    '''<g fill="#FFD700"><rect x="210" y="210" width="80" height="80" rx="15" transform="rotate(45 250 250)" fill="#8B0000"/><circle cx="250" cy="200" r="14" fill="#FFFFFF"/><circle cx="300" cy="250" r="14" fill="#FFFFFF"/><circle cx="250" cy="300" r="14" fill="#FFFFFF"/><circle cx="200" cy="250" r="14" fill="#FFFFFF"/></g>''',
    '''<g fill="#E85D75" opacity="0.9"><path d="M250,170 Q280,210 250,250 Q220,210 250,170 Z"/><path d="M250,330 Q280,290 250,250 Q220,290 250,330 Z"/><path d="M170,250 Q210,280 250,250 Q210,220 170,250 Z"/><path d="M330,250 Q290,280 250,250 Q290,220 330,250 Z"/></g>''',
    '''<g stroke="#FFD700" stroke-width="4" fill="#2C1609"><path d="M250,175 L275,225 L325,250 L275,275 L250,325 L225,275 L175,250 L225,225 Z"/></g>''',
    '''<g fill="#FFD700"><path d="M250,180 Q270,200 250,220 Q230,200 250,180 Z"/><path d="M250,220 Q265,240 255,270 Q245,290 260,295" fill="none" stroke="#FFD700" stroke-width="6"/><circle cx="235" cy="235" r="5" fill="#E85D75"/><circle cx="265" cy="235" r="5" fill="#E85D75"/></g>''',
    '''<g fill="#E85D75"><path d="M250,280 C210,230 200,190 230,180 C245,175 250,190 250,190 C250,190 255,175 270,180 C300,190 290,230 250,280 Z" transform="scale(1.2) translate(-42 -30)"/></g>'''
]

RAKHI_CONFIGS = [
    ("rakhi1", "#8B0000", "#FFD700", RAKHI_MOTIFS[0]),
    ("rakhi2", "#4A0E17", "#FF9933", RAKHI_MOTIFS[1]),
    ("rakhi3", "#004D40", "#FFFDD0", RAKHI_MOTIFS[2]),
    ("rakhi4", "#8B0000", "#FFD700", RAKHI_MOTIFS[3]),
    ("rakhi5", "#E85D75", "#FFD700", RAKHI_MOTIFS[4]),
    ("rakhi6", "#1A237E", "#FFD700", RAKHI_MOTIFS[5]),
    ("rakhi7", "#CC6600", "#FFD700", RAKHI_MOTIFS[6]),
    ("rakhi8", "#D81B60", "#FFD700", RAKHI_MOTIFS[7]),
]

SVG_AARTI_THALI = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <defs>
    <radialGradient id="brassGrad" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#FFF5B8"/>
      <stop offset="30%" stop-color="#FFD700"/>
      <stop offset="70%" stop-color="#DAA520"/>
      <stop offset="100%" stop-color="#8B6508"/>
    </radialGradient>
    <radialGradient id="thaliInner" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8B0000"/>
      <stop offset="70%" stop-color="#4A0E17"/>
      <stop offset="100%" stop-color="#2A0005"/>
    </radialGradient>
    <radialGradient id="flameLight" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="20%" stop-color="#FFFF00"/>
      <stop offset="60%" stop-color="#FF6600"/>
      <stop offset="100%" stop-color="#FF0000" stop-opacity="0"/>
    </radialGradient>
    <filter id="thaliShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <g filter="url(#thaliShadow)">
    <circle cx="300" cy="300" r="280" fill="url(#brassGrad)"/>
    <circle cx="300" cy="300" r="260" stroke="#8B6508" stroke-width="4" fill="none" stroke-dasharray="14 8"/>
    <circle cx="300" cy="300" r="240" fill="url(#brassGrad)"/>
    <circle cx="300" cy="300" r="225" fill="url(#thaliInner)"/>
    <circle cx="300" cy="300" r="200" stroke="#FFD700" stroke-width="1.5" fill="none" opacity="0.3"/>
    <circle cx="300" cy="300" r="150" stroke="#FFD700" stroke-width="1" stroke-dasharray="6 4" fill="none" opacity="0.3"/>
  </g>

  <!-- Diya -->
  <g transform="translate(300, 160)">
    <ellipse cx="0" cy="20" rx="45" ry="25" fill="url(#brassGrad)"/>
    <path d="M-40,15 Q0,40 40,15 Q0,-10 -40,15 Z" fill="#DAA520"/>
    <ellipse cx="0" cy="12" rx="30" ry="12" fill="#5C3A21"/>
    <circle cx="0" cy="-25" r="70" fill="url(#flameLight)" opacity="0.85"/>
    <path d="M-12,5 Q0,-50 12,5 Q0,15 -12,5 Z" fill="#FF9933"/>
    <path d="M-7,3 Q0,-40 7,3 Q0,10 -7,3 Z" fill="#FFD700"/>
    <path d="M-3,0 Q0,-25 3,0 Q0,5 -3,0 Z" fill="#FFFFFF"/>
  </g>

  <!-- Kumkum -->
  <g transform="translate(180, 270)">
    <circle cx="0" cy="0" r="32" fill="url(#brassGrad)"/>
    <circle cx="0" cy="0" r="26" fill="#8B0000"/>
    <circle cx="0" cy="0" r="24" fill="#D50000"/>
  </g>

  <!-- Rice -->
  <g transform="translate(420, 270)">
    <circle cx="0" cy="0" r="32" fill="url(#brassGrad)"/>
    <circle cx="0" cy="0" r="26" fill="#FFFDD0"/>
    <circle cx="-10" cy="-6" r="3" fill="#FFFFFF"/><circle cx="5" cy="-10" r="3.5" fill="#FFFDD0"/>
    <circle cx="12" cy="4" r="3" fill="#FFFFFF"/><circle cx="2" cy="8" r="3.5" fill="#FFD700"/>
  </g>

  <!-- Rakhi in Thali -->
  <g transform="translate(300, 360) scale(0.65)">
    <path d="M-180,0 Q-90,-40 0,0 Q90,40 180,0" stroke="#FFD700" stroke-width="8" fill="none"/>
    <path d="M-180,0 Q-90,40 0,0 Q90,-40 180,0" stroke="#E85D75" stroke-width="8" fill="none"/>
    <circle cx="0" cy="0" r="50" fill="url(#brassGrad)"/>
    <circle cx="0" cy="0" r="40" fill="#8B0000"/>
    <polygon points="0,-30 8,-10 30,-10 12,5 20,25 0,12 -20,25 -12,5 -30,-10 -8,-10" fill="#FFD700"/>
    <circle cx="0" cy="0" r="12" fill="#FFFFFF"/>
  </g>

  <!-- Flowers & Incense -->
  <g>
    <g transform="translate(230, 420)">
      <circle cx="0" cy="0" r="18" fill="#FF9933"/>
      <circle cx="0" cy="0" r="14" fill="#FFD700"/>
      <circle cx="0" cy="0" r="8" fill="#CC6600"/>
    </g>
    <g transform="translate(370, 420)">
      <circle cx="0" cy="0" r="18" fill="#FF9933"/>
      <circle cx="0" cy="0" r="14" fill="#FFD700"/>
      <circle cx="0" cy="0" r="8" fill="#CC6600"/>
    </g>
    <path d="M210,210 C190,200 180,220 200,230 C210,235 220,220 210,210 Z" fill="#E85D75"/>
    <path d="M390,210 C410,200 420,220 400,230 C390,235 380,220 390,210 Z" fill="#E85D75"/>
  </g>
</svg>'''

SWEET_KAJU_KATLI = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="silverVark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="30%" stop-color="#E0E0E0"/>
      <stop offset="70%" stop-color="#B0B0B0"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <linearGradient id="kajuBase" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFDD0"/>
      <stop offset="100%" stop-color="#F5E6C8"/>
    </linearGradient>
  </defs>
  <circle cx="200" cy="200" r="180" fill="#DAA520" opacity="0.2"/>
  <g filter="drop-shadow(0px 8px 10px rgba(0,0,0,0.4))">
    <polygon points="200,90 280,180 200,270 120,180" fill="url(#kajuBase)"/>
    <polygon points="200,90 280,180 200,270 120,180" fill="url(#silverVark)" opacity="0.75"/>
    <polygon points="270,140 350,230 270,320 190,230" fill="url(#kajuBase)"/>
    <polygon points="270,140 350,230 270,320 190,230" fill="url(#silverVark)" opacity="0.6"/>
    <polygon points="130,140 210,230 130,320 50,230" fill="url(#kajuBase)"/>
    <polygon points="130,140 210,230 130,320 50,230" fill="url(#silverVark)" opacity="0.8"/>
  </g>
</svg>'''

SWEET_GULAB_JAMUN = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="gjGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#A0522D"/>
      <stop offset="40%" stop-color="#5C2408"/>
      <stop offset="85%" stop-color="#2C0C00"/>
      <stop offset="100%" stop-color="#120300"/>
    </radialGradient>
  </defs>
  <circle cx="200" cy="210" r="160" fill="#B8860B"/>
  <circle cx="200" cy="210" r="145" fill="#4A0E17"/>
  <g filter="drop-shadow(0px 8px 10px rgba(0,0,0,0.5))">
    <circle cx="150" cy="180" r="55" fill="url(#gjGrad)"/>
    <circle cx="250" cy="180" r="55" fill="url(#gjGrad)"/>
    <circle cx="200" cy="235" r="60" fill="url(#gjGrad)"/>
  </g>
</svg>'''

SWEET_RASGULLA = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="rgGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#FFFDD0"/>
      <stop offset="100%" stop-color="#D7C4A5"/>
    </radialGradient>
  </defs>
  <circle cx="200" cy="210" r="150" fill="#E0F7FA" opacity="0.4"/>
  <g filter="drop-shadow(0px 6px 8px rgba(0,0,0,0.3))">
    <circle cx="155" cy="185" r="52" fill="url(#rgGrad)"/>
    <circle cx="245" cy="185" r="52" fill="url(#rgGrad)"/>
    <circle cx="200" cy="235" r="58" fill="url(#rgGrad)"/>
  </g>
</svg>'''

SWEET_LADOO = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="ladooGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FFE066"/>
      <stop offset="40%" stop-color="#FF9933"/>
      <stop offset="100%" stop-color="#803300"/>
    </radialGradient>
  </defs>
  <g filter="drop-shadow(0px 8px 10px rgba(0,0,0,0.4))">
    <circle cx="200" cy="210" r="110" fill="url(#ladooGrad)"/>
    <g fill="#FFD700" opacity="0.8">
      <circle cx="160" cy="160" r="8"/><circle cx="185" cy="145" r="9"/><circle cx="220" cy="155" r="7"/>
      <circle cx="245" cy="180" r="9"/><circle cx="140" cy="195" r="10"/><circle cx="170" cy="220" r="9"/>
    </g>
  </g>
</svg>'''

SWEET_BARFI = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <rect x="110" y="140" width="180" height="140" rx="10" fill="#81C784"/>
  <rect x="110" y="140" width="180" height="70" rx="10" fill="#FFFFFF" opacity="0.7"/>
</svg>'''

SWEET_JALEBI = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <g stroke="#FF9933" stroke-width="22" stroke-linecap="round" fill="none" filter="drop-shadow(0px 8px 10px rgba(0,0,0,0.4))">
    <path d="M160,180 C140,140 210,130 220,180 C230,220 150,230 140,170 C130,120 240,110 250,190"/>
    <path d="M210,220 C190,180 260,170 270,220 C280,260 200,270 190,210 C180,160 290,150 300,230"/>
  </g>
</svg>'''

SVG_GIFT_BOX = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="boxBody" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E85D75"/>
      <stop offset="50%" stop-color="#8B0000"/>
      <stop offset="100%" stop-color="#4A0E17"/>
    </linearGradient>
    <linearGradient id="goldRibbon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF5B8"/>
      <stop offset="50%" stop-color="#FFD700"/>
      <stop offset="100%" stop-color="#B8860B"/>
    </linearGradient>
  </defs>

  <g filter="drop-shadow(0px 16px 16px rgba(0,0,0,0.5))">
    <rect x="100" y="220" width="300" height="210" rx="16" fill="url(#boxBody)"/>
    <rect x="225" y="220" width="50" height="210" fill="url(#goldRibbon)"/>
    
    <g class="gift-lid-group">
      <rect x="80" y="170" width="340" height="65" rx="12" fill="url(#boxBody)"/>
      <rect x="225" y="170" width="50" height="65" fill="url(#goldRibbon)"/>
      
      <g transform="translate(250, 165)" fill="url(#goldRibbon)">
        <path d="M0,0 C-70,-60 -80,20 0,0 Z"/>
        <path d="M0,0 C70,-60 80,20 0,0 Z"/>
        <circle cx="0" cy="0" r="20" fill="#FFF5B8"/>
      </g>
    </g>
  </g>
</svg>'''

def make_gift_icon_svg(name, icon_content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="100%" height="100%">
  <rect width="300" height="300" rx="30" fill="#4A0E17"/>
  <circle cx="150" cy="150" r="120" stroke="#FFD700" stroke-width="4" fill="none" stroke-dasharray="8 6"/>
  <g transform="translate(150, 150)">
    {icon_content}
  </g>
</svg>'''

GIFT_ICONS = {
    "phone": '<rect x="-45" y="-80" width="90" height="160" rx="16" fill="#1A1A1A" stroke="#FFD700" stroke-width="4"/><rect x="-38" y="-65" width="76" height="130" rx="6" fill="#8B0000"/><circle cx="0" cy="72" r="5" fill="#FFD700"/>',
    "laptop": '<rect x="-70" y="-60" width="140" height="90" rx="8" fill="#2C2C2C" stroke="#FFD700" stroke-width="4"/><path d="M-90,30 L90,30 L75,50 L-75,50 Z" fill="#DAA520"/><rect x="-55" y="-45" width="110" height="65" fill="#FF9933" opacity="0.8"/>',
    "headphones": '<path d="M-60,0 A60,60 0 0,1 60,0" fill="none" stroke="#FFD700" stroke-width="12" stroke-linecap="round"/><rect x="-75" y="-10" width="30" height="50" rx="10" fill="#E85D75"/><rect x="45" y="-10" width="30" height="50" rx="10" fill="#E85D75"/>',
    "shopping": '<path d="M-50,-20 L-40,-70 L40,-70 L50,-20 Z" fill="none" stroke="#FFD700" stroke-width="8"/><rect x="-60" y="-20" width="120" height="100" rx="12" fill="#E85D75"/><path d="M-20,-20 L-20,10 M20,-20 L20,10" stroke="#FFD700" stroke-width="6"/>',
    "cash": '<rect x="-70" y="-45" width="140" height="90" rx="8" fill="#4CAF50" stroke="#FFD700" stroke-width="4"/><circle cx="0" cy="0" r="25" fill="#8BC34A"/><text x="0" y="10" font-size="30" font-weight="bold" fill="#FFF" text-anchor="middle">₹</text>',
    "chocolates": '<rect x="-60" y="-50" width="120" height="100" rx="10" fill="#3E2723" stroke="#FFD700" stroke-width="4"/><rect x="-45" y="-35" width="40" height="35" fill="#5D4037"/><rect x="5" y="-35" width="40" height="35" fill="#5D4037"/><rect x="-45" y="10" width="40" height="35" fill="#5D4037"/><rect x="5" y="10" width="40" height="35" fill="#5D4037"/>',
    "trip": '<path d="M-70,20 Q0,-80 70,20 Q0,-10 -70,20 Z" fill="#FFD700"/><path d="M-40,10 L0,-50 L40,10 Z" fill="#E85D75"/><circle cx="0" cy="50" r="30" fill="none" stroke="#FFF" stroke-width="4"/>',
    "surprise": '<rect x="-50" y="-50" width="100" height="100" rx="12" fill="#E85D75" stroke="#FFD700" stroke-width="4"/><text x="0" y="25" font-size="70" font-weight="bold" fill="#FFD700" text-anchor="middle">?</text>'
}

def main():
    ensure_dirs()
    print("Generating sound files...")
    generate_audio_files()

    print("Writing SVG assets...")
    with open('images/brother-sister.svg', 'w', encoding='utf-8') as f:
        f.write(SVG_BROTHER_SISTER)

    for name, main_c, acc_c, motif in RAKHI_CONFIGS:
        idx = name.replace("rakhi", "")
        filename = f'images/rakhi-{idx}.svg'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(make_rakhi_svg(name, main_c, acc_c, motif))

    with open('images/aarti-thali.svg', 'w', encoding='utf-8') as f:
        f.write(SVG_AARTI_THALI)

    with open('images/kaju-katli.svg', 'w', encoding='utf-8') as f:
        f.write(SWEET_KAJU_KATLI)
    with open('images/gulab-jamun.svg', 'w', encoding='utf-8') as f:
        f.write(SWEET_GULAB_JAMUN)
    with open('images/rasgulla.svg', 'w', encoding='utf-8') as f:
        f.write(SWEET_RASGULLA)
    with open('images/ladoo.svg', 'w', encoding='utf-8') as f:
        f.write(SWEET_LADOO)
    with open('images/barfi.svg', 'w', encoding='utf-8') as f:
        f.write(SWEET_BARFI)
    with open('images/jalebi.svg', 'w', encoding='utf-8') as f:
        f.write(SWEET_JALEBI)

    with open('images/gift-box.svg', 'w', encoding='utf-8') as f:
        f.write(SVG_GIFT_BOX)

    for g_name, g_svg in GIFT_ICONS.items():
        with open(f'images/{g_name}.svg', 'w', encoding='utf-8') as f:
            f.write(make_gift_icon_svg(g_name, g_svg))

    print("All assets generated successfully!")

if __name__ == '__main__':
    main()
