def FLTINFO(year):
    create = """CREATE TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """](
	[ID] [int] NOT NULL,
	[OPERATOR] [nvarchar](3) NULL,
	[FLT_NR] [int] NULL,
	[AC_REGISTRATION] [nvarchar](10) NULL,
	[FROM_IATA] [nvarchar](3) NULL,
	[TO_IATA] [nvarchar](3) NULL,
	[DIV_IATA] [nvarchar](3) NULL,
	[STD] [datetime] NULL,
	[ETD] [datetime] NULL,
	[ATD] [datetime] NULL,
	[STA] [datetime] NULL,
	[ETA] [datetime] NULL,
	[ATA] [datetime] NULL,
	[ONBLOCK] [datetime] NULL,
	[FROM_TERMINAL] [nvarchar](5) NULL,
	[FROM_GATE] [nvarchar](10) NULL,
	[FROM_STAND] [nvarchar](10) NULL,
	[TO_TERMINAL] [nvarchar](5) NULL,
	[TO_STAND] [nvarchar](10) NULL,
	[TO_BELT] [nvarchar](10) NULL,
	[DOOROPEN] [datetime] NULL,
	[DOORCLOSED] [datetime] NULL,
	[ASSIGNUSER] [int] NULL,
	[ISOTPDISMISS] [bit] NULL,
	[CF] [nvarchar](1) NULL,
	[DBAGM] [nvarchar](1) NULL,
	[DTT] [nvarchar](1) NULL,
	[DH2H] [nvarchar](1) NULL,
	[ALT] [nvarchar](1) NULL,
	[ABAGM] [nvarchar](1) NULL,
 CONSTRAINT [OSPRK_OSUSR_UUK_FLT_INFO""" + year + """] PRIMARY KEY CLUSTERED 
(
	[ID]
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [OPERATOR]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ((0)) FOR [FLT_NR]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [AC_REGISTRATION]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [FROM_IATA]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [TO_IATA]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [DIV_IATA]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [STD]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETD]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ATD]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [STA]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETA]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ATA]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ONBLOCK]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [FROM_TERMINAL]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [FROM_GATE]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [FROM_STAND]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [TO_TERMINAL]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [TO_STAND]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [TO_BELT]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [DOOROPEN]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [DOORCLOSED]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT (NULL) FOR [ASSIGNUSER]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ((0)) FOR [ISOTPDISMISS]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [CF]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [DBAGM]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [DTT]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [DH2H]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [ALT]
ALTER TABLE [dbo].[OSUSR_UUK_FLT_INFO""" + year + """] ADD  DEFAULT ('') FOR [ABAGM]

"""
    return create