-- 1. 사용자 테이블
CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    current_role VARCHAR(100),
    years_of_experience INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. 사용자 이력서/프로필 테이블
CREATE TABLE resumes (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    title VARCHAR(200) NOT NULL,
    raw_content LONGTEXT NOT NULL,          -- 이력서 전문
    parsed_skills JSON,                    -- 파싱된 스킬 태그 (예: ["Python", "FastAPI", "Docker"])
    experience_summary TEXT,               -- 경력 요약
    is_primary BOOLEAN DEFAULT FALSE,      -- 대표 이력서 여부
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 3. 채용 공고 마스터 테이블 (RDB 동기화용 기본 메타)
CREATE TABLE job_postings (
    id VARCHAR(64) PRIMARY KEY,             -- 크롤링 고유 ID or UUID (ES _id와 일치)
    company_name VARCHAR(150) NOT NULL,
    title VARCHAR(255) NOT NULL,
    location VARCHAR(100),
    experience_level VARCHAR(50),          -- 신입 / 경력(연차)
    source_url VARCHAR(500),
    closing_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 4. 역량 갭 분석 리포트 (Gemini 생성 결과물)
CREATE TABLE gap_reports (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    resume_id BIGINT NOT NULL,
    job_posting_id VARCHAR(64) NOT NULL,
    match_score DECIMAL(5, 2),             -- 종합 매칭 점수 (예: 78.50%)
    matched_skills JSON,                   -- 충족된 역량
    missing_skills JSON,                   -- 부족한 역량
    ai_feedback LONGTEXT,                  -- Gemini가 작성한 역량 보완 가이드
    roadmap_recommendation JSON,           -- 학습 추천 로드맵 (단계별 액션 플랜)
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (resume_id) REFERENCES resumes(id) ON DELETE CASCADE,
    FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE
);

-- 5. 공고 북마크/관심 공고
CREATE TABLE user_job_bookmarks (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    job_posting_id VARCHAR(64) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_user_job (user_id, job_posting_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE
);