import os
import re

preloader_style = """
        /* [PRO SKELETON PRELOADER] */
        #bt_preloader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: #222222;
            z-index: 9999999;
            display: flex;
            flex-direction: column;
            padding: 0;
            margin: 0;
            box-sizing: border-box;
            transition: opacity 0.5s ease, visibility 0.5s ease;
        }

        #bt_preloader.loaded {
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
        }

        /* Top White Header Bar */
        .sk-header {
            background: #ffffff;
            height: 100px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 30px;
            box-sizing: border-box;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            flex-shrink: 0;
        }

        .sk-logo { width: 180px; height: 50px; }
        .sk-nav { width: 34px; height: 34px; border-radius: 5px; }

        /* Dark Hero Content */
        .sk-hero {
            flex: 1;
            background: #000000;
            padding: 50px 30px;
            display: flex;
            flex-direction: column;
        }

        .sk-shimmer {
            background: #222222;
            background-image: linear-gradient(90deg, #222222 0px, #333333 40px, #222222 80px);
            background-size: 600px;
            animation: sk-shimmer 1.5s infinite linear;
            border-radius: 4px;
        }

        .sk-shimmer-light {
            background: #f4f4f4;
            background-image: linear-gradient(90deg, #f4f4f4 0px, #e8e8e8 40px, #f4f4f4 80px);
            background-size: 600px;
            animation: sk-shimmer 1.5s infinite linear;
            border-radius: 4px;
        }

        @keyframes sk-shimmer {
            0% { background-position: -200px 0; }
            100% { background-position: 400px 0; }
        }

        .sk-line-lg { width: 80%; height: 50px; margin-bottom: 20px; }
        .sk-line-md { width: 60%; height: 50px; margin-bottom: 40px; }
        .sk-line-sm { width: 90%; height: 18px; margin-bottom: 12px; }
        .sk-line-xs { width: 70%; height: 18px; margin-bottom: 50px; }
        .sk-btn { width: 170px; height: 50px; border-radius: 25px; }

        @media (min-width: 992px) {
            .sk-header { padding: 0 10%; height: 100px; }
            .sk-hero { padding: 15% 10%; }
            .sk-line-lg { width: 600px; height: 65px; }
            .sk-line-md { width: 450px; height: 65px; }
            .sk-line-sm { width: 500px; }
            .sk-line-xs { width: 400px; }
            .sk-nav { display: none; }
        }
"""

preloader_html = """
    <!-- Premium Skeleton Preloader -->
    <div id="bt_preloader">
        <div class="sk-header">
            <div class="sk-logo sk-shimmer-light"></div>
            <div class="sk-nav sk-shimmer-light"></div>
        </div>
        <div class="sk-hero">
            <div class="sk-line-lg sk-shimmer"></div>
            <div class="sk-line-md sk-shimmer"></div>
            <div class="sk-line-sm sk-shimmer"></div>
            <div class="sk-line-sm sk-shimmer"></div>
            <div class="sk-line-xs sk-shimmer"></div>
            <div class="sk-btn sk-shimmer"></div>
        </div>
    </div>
"""

preloader_script = """
    <!-- Preloader Script -->
    <script>
        window.addEventListener('load', function() {
            var preloader = document.getElementById('bt_preloader');
            if (preloader) {
                setTimeout(function() {
                    preloader.classList.add('loaded');
                }, 400);
            }
        });
    </script>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old HTML components
    content = re.sub(r'<!-- Skeleton Preloader -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Premium Skeleton Preloader -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)

    # Remove old style blocks
    content = re.sub(r'/\* \[SKELETON PRELOADER\] \*/.*?(?=</style>)', '', content, flags=re.DOTALL)
    content = re.sub(r'/\* \[PRO SKELETON PRELOADER\] \*/.*?(?=</style>)', '', content, flags=re.DOTALL)
    
    # Remove old script blocks
    content = re.sub(r'<!-- Preloader Script -->\s*<script>\s*window\.addEventListener.*?</script>', '', content, flags=re.DOTALL)

    # Optional: cleanup empty spaces created by regexes
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    # 1. Insert New Style
    style_tag_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
    if style_tag_match:
         content = content.replace('</style>', preloader_style + '    </style>', 1)
    else:
         content = content.replace('</head>', '    <style>' + preloader_style + '    </style>\n</head>', 1)
    
    # 2. Insert New HTML
    body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
    if body_match:
        pos = body_match.end()
        content = content[:pos] + preloader_html + content[pos:]
    
    # 3. Insert New Script
    if '</body>' in content:
        content = content.replace('</body>', preloader_script + '\n</body>', 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        process_file(filename)
