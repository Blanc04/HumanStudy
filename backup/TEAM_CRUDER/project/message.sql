CREATE TABLE notice (
	notice_id	int	NOT NULL,
	notice_title	varchar(200)	NULL,
	notice_detail	varchar(2000)	NULL,
	notice_date	datetime	NULL,
	user_id	varchar(12)	NOT NULL
);

CREATE TABLE api_sync_log (
	sync_log_id	BIGINT	NOT NULL,
	called_at	datetime	NULL,
	result_code	varchar(20)	NULL,
	result_message	varchar(255)	NULL,
	total_count	int	NULL,
	success_count	int	NULL,
	fail_count	int	NULL,
	error_message	text	NULL
);

CREATE TABLE inquiry (
	inquiry_id	int	NOT NULL,
	inquiry_title	varchar(100)	NULL,
	inquiry_detail	varchar(5000)	NULL,
	inquiry_date	datetime	NULL,
	inquiry_answer	varchar(2000)	NULL,
	inquiry_answer_date	date	NULL,
	user_id	varchar(12)	NOT NULL,
	inquiry_status_id	int	NOT NULL,
	inquiry_type	varchar(5)	NULL
);

CREATE TABLE ai_chat_message (
	ai_chat_message_id	int	NOT NULL,
	ai_chat_detail	text	NULL,
	ai_chat_id	int	NOT NULL
);

CREATE TABLE user (
	user_id	varchar(12)	NOT NULL,
	user_name	varchar(20)	NULL,
	user_pw	varchar(255)	NULL,
	user_phone	varchar(30)	NULL,
	user_status_id	int	NOT NULL,
	user_home	varchar(50)	NULL,
	user_email	varchar(40)	NULL
);

CREATE TABLE job_tip (
	job_tip_no	int	NOT NULL,
	job_tip_title	varchar(200)	NULL,
	job_tip_date	datetime	NULL,
	job_tip_detail	text	NULL,
	job_tip_attachment	text	NULL,
	user_id	varchar(12)	NOT NULL
);

CREATE TABLE report_logs (
	report_id	BIGINT	NOT NULL,
	report_reason	varchar(120)	NULL,
	user_id	varchar(12)	NOT NULL,
	job_tip_no	int	NULL
);

CREATE TABLE job_tip_comment (
	reple_no	int	NOT NULL,
	reple	varchar(500)	NULL,
	parent_reple_no	int	NULL,
	job_tip_no	int	NOT NULL,
	user_id	varchar(12)	NOT NULL
);

CREATE TABLE ai_chat_result (
	ai_chat_result_id	int	NOT NULL,
	recrut_pblnt_sn	varchar(20)	NOT NULL,
	ai_chat_message_id	int	NOT NULL
);

CREATE TABLE user_status (
	user_status_id	int	NOT NULL,
	user_status_name	varchar(5)	NULL,
	user_status_code	int	NULL
);

CREATE TABLE ai_chat_room (
	ai_chat_id	int	NOT NULL,
	ai_chat_date	date	NULL,
	user_id	varchar(12)	NOT NULL
);

CREATE TABLE jobs (
	recrut_pblnt_sn	varchar(20)	NOT NULL,
	recrut_bbanc_ttl	varchar(100)	NULL,
	inst_nm	varchar(100)	NULL,
	pbanc_bgng_ymd	DATE	NULL,
	pbanc_end_ymd	DATE	NULL,
	src_url	varchar(500)	NULL,
	ongoing_yn	char(1)	NULL,
	recrut_se_nm	varchar(50)	NULL,
	recrut_nope	int	NULL,
	work_rgn_nm_lst	varchar(100)	NULL
);

CREATE TABLE inquiry_status (
	inquiry_status_id	int	NOT NULL,
	inquiry_status_name	varchar(5)	NULL
);

CREATE TABLE bookmark (
	user_id	varchar(12)	NOT NULL,
	recrut_pblnt_sn	varchar(20)	NOT NULL
);

ALTER TABLE notice ADD CONSTRAINT PK_NOTICE PRIMARY KEY (
	notice_id
);

ALTER TABLE api_sync_log ADD CONSTRAINT PK_API_SYNC_LOG PRIMARY KEY (
	sync_log_id
);

ALTER TABLE inquiry ADD CONSTRAINT PK_INQUIRY PRIMARY KEY (
	inquiry_id
);

ALTER TABLE ai_chat_message ADD CONSTRAINT PK_AI_CHAT_MESSAGE PRIMARY KEY (
	ai_chat_message_id
);

ALTER TABLE user ADD CONSTRAINT PK_USER PRIMARY KEY (
	user_id
);

ALTER TABLE job_tip ADD CONSTRAINT PK_JOB_TIP PRIMARY KEY (
	job_tip_no
);

ALTER TABLE report_logs ADD CONSTRAINT PK_REPORT_LOGS PRIMARY KEY (
	report_id
);

ALTER TABLE job_tip_comment ADD CONSTRAINT PK_JOB_TIP_COMMENT PRIMARY KEY (
	reple_no
);

ALTER TABLE ai_chat_result ADD CONSTRAINT PK_AI_CHAT_RESULT PRIMARY KEY (
	ai_chat_result_id
);

ALTER TABLE user_status ADD CONSTRAINT PK_USER_STATUS PRIMARY KEY (
	user_status_id
);

ALTER TABLE ai_chat_room ADD CONSTRAINT PK_AI_CHAT_ROOM PRIMARY KEY (
	ai_chat_id
);

ALTER TABLE jobs ADD CONSTRAINT PK_JOBS PRIMARY KEY (
	recrut_pblnt_sn
);

ALTER TABLE inquiry_status ADD CONSTRAINT PK_INQUIRY_STATUS PRIMARY KEY (
	inquiry_status_id
);

ALTER TABLE bookmark ADD CONSTRAINT PK_BOOKMARK PRIMARY KEY (
	user_id,
	recrut_pblnt_sn
);

ALTER TABLE notice ADD CONSTRAINT FK_user_TO_notice_1 FOREIGN KEY (
	user_id
)
REFERENCES user (
	user_id
);

ALTER TABLE inquiry ADD CONSTRAINT FK_user_TO_inquiry_1 FOREIGN KEY (
	user_id
)
REFERENCES user (
	user_id
);

ALTER TABLE inquiry ADD CONSTRAINT FK_inquiry_status_TO_inquiry_1 FOREIGN KEY (
	inquiry_status_id
)
REFERENCES inquiry_status (
	inquiry_status_id
);

ALTER TABLE ai_chat_message ADD CONSTRAINT FK_ai_chat_room_TO_ai_chat_message_1 FOREIGN KEY (
	ai_chat_id
)
REFERENCES ai_chat_room (
	ai_chat_id
);

ALTER TABLE user ADD CONSTRAINT FK_user_status_TO_user_1 FOREIGN KEY (
	user_status_id
)
REFERENCES user_status (
	user_status_id
);

ALTER TABLE job_tip ADD CONSTRAINT FK_user_TO_job_tip_1 FOREIGN KEY (
	user_id
)
REFERENCES user (
	user_id
);

ALTER TABLE report_logs ADD CONSTRAINT FK_user_TO_report_logs_1 FOREIGN KEY (
	user_id
)
REFERENCES user (
	user_id
);

ALTER TABLE report_logs ADD CONSTRAINT FK_job_tip_TO_report_logs_1 FOREIGN KEY (
	job_tip_no
)
REFERENCES job_tip (
	job_tip_no
);

ALTER TABLE job_tip_comment ADD CONSTRAINT FK_job_tip_comment_TO_job_tip_comment_1 FOREIGN KEY (
	parent_reple_no
)
REFERENCES job_tip_comment (
	reple_no
);

ALTER TABLE job_tip_comment ADD CONSTRAINT FK_job_tip_TO_job_tip_comment_1 FOREIGN KEY (
	job_tip_no
)
REFERENCES job_tip (
	job_tip_no
);

ALTER TABLE job_tip_comment ADD CONSTRAINT FK_user_TO_job_tip_comment_1 FOREIGN KEY (
	user_id
)
REFERENCES user (
	user_id
);

ALTER TABLE ai_chat_result ADD CONSTRAINT FK_jobs_TO_ai_chat_result_1 FOREIGN KEY (
	recrut_pblnt_sn
)
REFERENCES jobs (
	recrut_pblnt_sn
);

ALTER TABLE ai_chat_result ADD CONSTRAINT FK_ai_chat_message_TO_ai_chat_result_1 FOREIGN KEY (
	ai_chat_message_id
)
REFERENCES ai_chat_message (
	ai_chat_message_id
);

ALTER TABLE ai_chat_room ADD CONSTRAINT FK_user_TO_ai_chat_room_1 FOREIGN KEY (
	user_id
)
REFERENCES user (
	user_id
);

ALTER TABLE bookmark ADD CONSTRAINT FK_user_TO_bookmark_1 FOREIGN KEY (
	user_id
)
REFERENCES user (
	user_id
);

ALTER TABLE bookmark ADD CONSTRAINT FK_jobs_TO_bookmark_1 FOREIGN KEY (
	recrut_pblnt_sn
)
REFERENCES jobs (
	recrut_pblnt_sn
);