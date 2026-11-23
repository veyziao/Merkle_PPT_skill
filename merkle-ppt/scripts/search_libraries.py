#!/usr/bin/env python3
"""Find candidate Merkle reference pages/icons; inspect source before selection."""
import argparse
import json
import re
from pathlib import Path

REF = Path(__file__).resolve().parents[1] / 'references'
LIBS = {
    'slide': ('slide-library-index.json', 'slides'),
    'qbr': ('qbr-slide-library-index.json', 'slides'),
    'case': ('case-library-index.json', 'slides'),
    'diagram': ('diagram-library-index.json', 'entries'),
    'icon': ('merkle-icon-index.json', 'icons'),
}
# Expansion provides a transparent candidate list, not semantic verification.
GROUPS = [
    ('项目周报','项目进展','项目状态','阶段汇报','阶段总结','项目汇报','project update','status report','进度'),
    ('业务回顾','经营复盘','业绩回顾','阶段复盘','qbr','business review','绩效','kpi'),
    ('指标','绩效','成果','健康度','kpi','metrics','performance'),
    ('行动项','待办','下一步','负责人','action items','next steps'),
    ('时间线','路线图','里程碑','排期','计划','roadmap','timeline'),
    ('洞察','发现','经验','复盘','insight','learning','retrospective'),
    ('客户案例','案例','成功案例','case study','client story'),
    ('架构','数据流','系统关系','技术流程','architecture','data flow'),
    ('决策','建议','方案','recommendation','decision'),
    ('测试','试点','实验','验证','test','pilot','experiment'),
]

def strings(value):
    if isinstance(value, list): return ' '.join(strings(v) for v in value)
    if isinstance(value, dict): return ' '.join(strings(v) for v in value.values())
    return str(value or '')

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('query', help='Page purpose, concept or keyword')
    ap.add_argument('--library', choices=['all', *LIBS], default='all')
    ap.add_argument('--limit', type=int, default=15)
    args = ap.parse_args()
    if args.limit < 1: ap.error('--limit must be positive')
    query = args.query.strip().lower()
    if not query: ap.error('query cannot be empty')
    words = {query, *re.findall(r'[\u4e00-\u9fff]+|[a-z0-9-]+', query)}
    for group in GROUPS:
        if any(g in query for g in group): words.update(group)
    candidates = []
    for lib, (file, key) in LIBS.items():
        if args.library != 'all' and args.library != lib: continue
        for item in json.loads((REF / file).read_text(encoding='utf-8'))[key]:
            core = ' '.join(strings(item.get(k)) for k in ('id','title','category','name_zh','official_name','scenario','scenarios')).lower()
            rest = ' '.join(strings(item.get(k)) for k in ('composition','application','styling','english_tags')).lower()
            score = sum((3 if term in core else 0) + (1 if term in rest else 0) for term in words if len(term) >= 2)
            if score:
                title = item.get('title') or item.get('name_zh') or item.get('official_name') or ''
                candidates.append((score,lib,item['id'],item.get('page',item.get('slide')),title))
    candidates.sort(key=lambda x: (-x[0], x[1], str(x[2])))
    print('Keyword candidates; inspect source page and content fit before selection.')
    for score,lib,ident,page,title in candidates[:args.limit]: print(f'{lib}\t{ident}\tpage {page}\t{title}\tscore {score}')
    if not candidates: print('No keyword candidates; try related terms or inspect the index.')

if __name__ == '__main__': main()
