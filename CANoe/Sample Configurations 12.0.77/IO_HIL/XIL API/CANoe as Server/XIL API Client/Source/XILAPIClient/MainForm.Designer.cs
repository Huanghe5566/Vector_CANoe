namespace XILAPIClient
{
  partial class MainForm
  {
    /// <summary>
    /// Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    /// Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
      if (disposing && (components != null))
      {
        components.Dispose();
      }
      base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    /// Required method for Designer support - do not modify
    /// the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
      this.components = new System.ComponentModel.Container();
      System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
      this.mBtnConnect = new System.Windows.Forms.Button();
      this.mLblCurValue = new System.Windows.Forms.Label();
      this.mBarCurValue = new System.Windows.Forms.ProgressBar();
      this.mBtnDisconnect = new System.Windows.Forms.Button();
      this.mTimer = new System.Windows.Forms.Timer(this.components);
      this.mNumCurValue = new System.Windows.Forms.NumericUpDown();
      this.mTableLayoutPanel = new System.Windows.Forms.TableLayoutPanel();
      this.mPnlTop = new System.Windows.Forms.Panel();
      this.groupBox2 = new System.Windows.Forms.GroupBox();
      this.groupBox1 = new System.Windows.Forms.GroupBox();
      this.cbxProductVersion = new System.Windows.Forms.ComboBox();
      this.cbxProduct = new System.Windows.Forms.ComboBox();
      this.cbxVendor = new System.Windows.Forms.ComboBox();
      this.label8 = new System.Windows.Forms.Label();
      this.label7 = new System.Windows.Forms.Label();
      this.label6 = new System.Windows.Forms.Label();
      this.label5 = new System.Windows.Forms.Label();
      this.label4 = new System.Windows.Forms.Label();
      this.label3 = new System.Windows.Forms.Label();
      this.label2 = new System.Windows.Forms.Label();
      this.label1 = new System.Windows.Forms.Label();
      this.mDividerLine = new System.Windows.Forms.Panel();
      this.mPnlBottom = new System.Windows.Forms.Panel();
      this.mBtnQuit = new System.Windows.Forms.Button();
      ((System.ComponentModel.ISupportInitialize)(this.mNumCurValue)).BeginInit();
      this.mTableLayoutPanel.SuspendLayout();
      this.mPnlTop.SuspendLayout();
      this.groupBox2.SuspendLayout();
      this.groupBox1.SuspendLayout();
      this.mPnlBottom.SuspendLayout();
      this.SuspendLayout();
      // 
      // mBtnConnect
      // 
      this.mBtnConnect.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
      this.mBtnConnect.Location = new System.Drawing.Point(232, 15);
      this.mBtnConnect.Name = "mBtnConnect";
      this.mBtnConnect.Size = new System.Drawing.Size(75, 23);
      this.mBtnConnect.TabIndex = 0;
      this.mBtnConnect.Text = "Connect";
      this.mBtnConnect.UseVisualStyleBackColor = true;
      this.mBtnConnect.Click += new System.EventHandler(this.OnBtnConnectClick);
      // 
      // mLblCurValue
      // 
      this.mLblCurValue.AutoSize = true;
      this.mLblCurValue.Location = new System.Drawing.Point(15, 26);
      this.mLblCurValue.Name = "mLblCurValue";
      this.mLblCurValue.Size = new System.Drawing.Size(54, 13);
      this.mLblCurValue.TabIndex = 1;
      this.mLblCurValue.Text = "Variable1:";
      // 
      // mBarCurValue
      // 
      this.mBarCurValue.Location = new System.Drawing.Point(75, 50);
      this.mBarCurValue.MarqueeAnimationSpeed = 1;
      this.mBarCurValue.Name = "mBarCurValue";
      this.mBarCurValue.Size = new System.Drawing.Size(362, 20);
      this.mBarCurValue.TabIndex = 3;
      // 
      // mBtnDisconnect
      // 
      this.mBtnDisconnect.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
      this.mBtnDisconnect.Enabled = false;
      this.mBtnDisconnect.Location = new System.Drawing.Point(313, 15);
      this.mBtnDisconnect.Name = "mBtnDisconnect";
      this.mBtnDisconnect.Size = new System.Drawing.Size(75, 23);
      this.mBtnDisconnect.TabIndex = 4;
      this.mBtnDisconnect.Text = "Disconnect";
      this.mBtnDisconnect.UseVisualStyleBackColor = true;
      this.mBtnDisconnect.Click += new System.EventHandler(this.OnMBtnDisconnectClick);
      // 
      // mTimer
      // 
      this.mTimer.Interval = 10;
      this.mTimer.Tick += new System.EventHandler(this.OnTimerTick);
      // 
      // mNumCurValue
      // 
      this.mNumCurValue.DecimalPlaces = 2;
      this.mNumCurValue.Enabled = false;
      this.mNumCurValue.Location = new System.Drawing.Point(75, 24);
      this.mNumCurValue.Name = "mNumCurValue";
      this.mNumCurValue.Size = new System.Drawing.Size(362, 20);
      this.mNumCurValue.TabIndex = 8;
      this.mNumCurValue.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
      // 
      // mTableLayoutPanel
      // 
      this.mTableLayoutPanel.ColumnCount = 1;
      this.mTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
      this.mTableLayoutPanel.Controls.Add(this.mPnlTop, 0, 0);
      this.mTableLayoutPanel.Controls.Add(this.mDividerLine, 0, 1);
      this.mTableLayoutPanel.Controls.Add(this.mPnlBottom, 0, 2);
      this.mTableLayoutPanel.Dock = System.Windows.Forms.DockStyle.Fill;
      this.mTableLayoutPanel.Location = new System.Drawing.Point(0, 0);
      this.mTableLayoutPanel.Name = "mTableLayoutPanel";
      this.mTableLayoutPanel.RowCount = 3;
      this.mTableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
      this.mTableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 1F));
      this.mTableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 50F));
      this.mTableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
      this.mTableLayoutPanel.Size = new System.Drawing.Size(481, 382);
      this.mTableLayoutPanel.TabIndex = 9;
      // 
      // mPnlTop
      // 
      this.mPnlTop.Controls.Add(this.groupBox2);
      this.mPnlTop.Controls.Add(this.groupBox1);
      this.mPnlTop.Controls.Add(this.label5);
      this.mPnlTop.Controls.Add(this.label4);
      this.mPnlTop.Controls.Add(this.label3);
      this.mPnlTop.Controls.Add(this.label2);
      this.mPnlTop.Controls.Add(this.label1);
      this.mPnlTop.Dock = System.Windows.Forms.DockStyle.Fill;
      this.mPnlTop.Location = new System.Drawing.Point(3, 3);
      this.mPnlTop.Name = "mPnlTop";
      this.mPnlTop.Size = new System.Drawing.Size(475, 325);
      this.mPnlTop.TabIndex = 10;
      // 
      // groupBox2
      // 
      this.groupBox2.Controls.Add(this.mBarCurValue);
      this.groupBox2.Controls.Add(this.mLblCurValue);
      this.groupBox2.Controls.Add(this.mNumCurValue);
      this.groupBox2.Location = new System.Drawing.Point(9, 212);
      this.groupBox2.Name = "groupBox2";
      this.groupBox2.Size = new System.Drawing.Size(456, 96);
      this.groupBox2.TabIndex = 14;
      this.groupBox2.TabStop = false;
      this.groupBox2.Text = "Data Exchange";
      // 
      // groupBox1
      // 
      this.groupBox1.Controls.Add(this.cbxProductVersion);
      this.groupBox1.Controls.Add(this.cbxProduct);
      this.groupBox1.Controls.Add(this.cbxVendor);
      this.groupBox1.Controls.Add(this.label8);
      this.groupBox1.Controls.Add(this.label7);
      this.groupBox1.Controls.Add(this.label6);
      this.groupBox1.Location = new System.Drawing.Point(9, 122);
      this.groupBox1.Name = "groupBox1";
      this.groupBox1.Size = new System.Drawing.Size(456, 84);
      this.groupBox1.TabIndex = 13;
      this.groupBox1.TabStop = false;
      this.groupBox1.Text = "Configuration";
      // 
      // cbxProductVersion
      // 
      this.cbxProductVersion.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
      this.cbxProductVersion.FormattingEnabled = true;
      this.cbxProductVersion.Items.AddRange(new object[] {
            "2.0.1"});
      this.cbxProductVersion.Location = new System.Drawing.Point(307, 42);
      this.cbxProductVersion.Name = "cbxProductVersion";
      this.cbxProductVersion.Size = new System.Drawing.Size(130, 21);
      this.cbxProductVersion.TabIndex = 6;
      // 
      // cbxProduct
      // 
      this.cbxProduct.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
      this.cbxProduct.FormattingEnabled = true;
      this.cbxProduct.Items.AddRange(new object[] {
            "CANoe32",
            "CANoe64"});
      this.cbxProduct.Location = new System.Drawing.Point(171, 42);
      this.cbxProduct.Name = "cbxProduct";
      this.cbxProduct.Size = new System.Drawing.Size(130, 21);
      this.cbxProduct.TabIndex = 5;
      // 
      // cbxVendor
      // 
      this.cbxVendor.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
      this.cbxVendor.FormattingEnabled = true;
      this.cbxVendor.Items.AddRange(new object[] {
            "Vector"});
      this.cbxVendor.Location = new System.Drawing.Point(18, 42);
      this.cbxVendor.Name = "cbxVendor";
      this.cbxVendor.Size = new System.Drawing.Size(147, 21);
      this.cbxVendor.TabIndex = 4;
      // 
      // label8
      // 
      this.label8.AutoSize = true;
      this.label8.Location = new System.Drawing.Point(304, 26);
      this.label8.Name = "label8";
      this.label8.Size = new System.Drawing.Size(63, 13);
      this.label8.TabIndex = 2;
      this.label8.Text = "XIL version:";
      // 
      // label7
      // 
      this.label7.AutoSize = true;
      this.label7.Location = new System.Drawing.Point(168, 26);
      this.label7.Name = "label7";
      this.label7.Size = new System.Drawing.Size(47, 13);
      this.label7.TabIndex = 1;
      this.label7.Text = "Product:";
      // 
      // label6
      // 
      this.label6.AutoSize = true;
      this.label6.Location = new System.Drawing.Point(15, 26);
      this.label6.Name = "label6";
      this.label6.Size = new System.Drawing.Size(44, 13);
      this.label6.TabIndex = 0;
      this.label6.Text = "Vendor:";
      // 
      // label5
      // 
      this.label5.AutoSize = true;
      this.label5.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(183)))), ((int)(((byte)(0)))), ((int)(((byte)(50)))));
      this.label5.Location = new System.Drawing.Point(76, 65);
      this.label5.Name = "label5";
      this.label5.Size = new System.Drawing.Size(351, 13);
      this.label5.TabIndex = 11;
      this.label5.Text = "3. Click \'Connect\' to establish a connection to the CANoe XIL API server.";
      // 
      // label4
      // 
      this.label4.AutoSize = true;
      this.label4.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(183)))), ((int)(((byte)(0)))), ((int)(((byte)(50)))));
      this.label4.Location = new System.Drawing.Point(76, 83);
      this.label4.Name = "label4";
      this.label4.Size = new System.Drawing.Size(368, 13);
      this.label4.TabIndex = 12;
      this.label4.Text = "4. The value of \'Variable1\' will be received from CANoe and displayed below.";
      // 
      // label3
      // 
      this.label3.AutoSize = true;
      this.label3.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(183)))), ((int)(((byte)(0)))), ((int)(((byte)(50)))));
      this.label3.Location = new System.Drawing.Point(76, 47);
      this.label3.Name = "label3";
      this.label3.Size = new System.Drawing.Size(300, 13);
      this.label3.TabIndex = 11;
      this.label3.Text = "2. Start CANoe and open the configuration \'XILAPIServer.cfg\'.";
      // 
      // label2
      // 
      this.label2.AutoSize = true;
      this.label2.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(183)))), ((int)(((byte)(0)))), ((int)(((byte)(50)))));
      this.label2.Location = new System.Drawing.Point(76, 16);
      this.label2.Name = "label2";
      this.label2.Size = new System.Drawing.Size(377, 26);
      this.label2.TabIndex = 10;
      this.label2.Text = "1. Make sure the Vector CANoe XIL API package is installed on this computer.\r\n   " +
    "  (this package can be found in the CANoe demo addons folder)";
      // 
      // label1
      // 
      this.label1.AutoSize = true;
      this.label1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(183)))), ((int)(((byte)(0)))), ((int)(((byte)(50)))));
      this.label1.Location = new System.Drawing.Point(19, 16);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(41, 13);
      this.label1.TabIndex = 9;
      this.label1.Text = "Usage:";
      // 
      // mDividerLine
      // 
      this.mDividerLine.BackColor = System.Drawing.Color.DarkGray;
      this.mDividerLine.Dock = System.Windows.Forms.DockStyle.Fill;
      this.mDividerLine.Location = new System.Drawing.Point(0, 331);
      this.mDividerLine.Margin = new System.Windows.Forms.Padding(0);
      this.mDividerLine.Name = "mDividerLine";
      this.mDividerLine.Size = new System.Drawing.Size(481, 1);
      this.mDividerLine.TabIndex = 0;
      // 
      // mPnlBottom
      // 
      this.mPnlBottom.BackColor = System.Drawing.SystemColors.Control;
      this.mPnlBottom.Controls.Add(this.mBtnConnect);
      this.mPnlBottom.Controls.Add(this.mBtnQuit);
      this.mPnlBottom.Controls.Add(this.mBtnDisconnect);
      this.mPnlBottom.Dock = System.Windows.Forms.DockStyle.Fill;
      this.mPnlBottom.Location = new System.Drawing.Point(0, 332);
      this.mPnlBottom.Margin = new System.Windows.Forms.Padding(0);
      this.mPnlBottom.Name = "mPnlBottom";
      this.mPnlBottom.Size = new System.Drawing.Size(481, 50);
      this.mPnlBottom.TabIndex = 1;
      // 
      // mBtnQuit
      // 
      this.mBtnQuit.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
      this.mBtnQuit.Location = new System.Drawing.Point(394, 15);
      this.mBtnQuit.Name = "mBtnQuit";
      this.mBtnQuit.Size = new System.Drawing.Size(75, 23);
      this.mBtnQuit.TabIndex = 0;
      this.mBtnQuit.Text = "Quit";
      this.mBtnQuit.UseVisualStyleBackColor = true;
      this.mBtnQuit.Click += new System.EventHandler(this.OnBtnQuitClick);
      // 
      // MainForm
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.BackColor = System.Drawing.Color.White;
      this.ClientSize = new System.Drawing.Size(481, 382);
      this.Controls.Add(this.mTableLayoutPanel);
      this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
      this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
      this.MaximizeBox = false;
      this.MinimizeBox = false;
      this.Name = "MainForm";
      this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Show;
      this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
      this.Text = "XIL API Client Example";
      this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.OnFormClosing);
      this.Load += new System.EventHandler(this.OnLoad);
      ((System.ComponentModel.ISupportInitialize)(this.mNumCurValue)).EndInit();
      this.mTableLayoutPanel.ResumeLayout(false);
      this.mPnlTop.ResumeLayout(false);
      this.mPnlTop.PerformLayout();
      this.groupBox2.ResumeLayout(false);
      this.groupBox2.PerformLayout();
      this.groupBox1.ResumeLayout(false);
      this.groupBox1.PerformLayout();
      this.mPnlBottom.ResumeLayout(false);
      this.ResumeLayout(false);

    }

    #endregion

    private System.Windows.Forms.Button mBtnConnect;
    private System.Windows.Forms.Label mLblCurValue;
    private System.Windows.Forms.ProgressBar mBarCurValue;
    private System.Windows.Forms.Button mBtnDisconnect;
    private System.Windows.Forms.Timer mTimer;
    private System.Windows.Forms.NumericUpDown mNumCurValue;
    private System.Windows.Forms.TableLayoutPanel mTableLayoutPanel;
    private System.Windows.Forms.Panel mDividerLine;
    private System.Windows.Forms.Button mBtnQuit;
    private System.Windows.Forms.Panel mPnlTop;
    private System.Windows.Forms.Panel mPnlBottom;
    private System.Windows.Forms.Label label2;
    private System.Windows.Forms.Label label1;
    private System.Windows.Forms.Label label5;
    private System.Windows.Forms.Label label4;
    private System.Windows.Forms.Label label3;
    private System.Windows.Forms.GroupBox groupBox2;
    private System.Windows.Forms.GroupBox groupBox1;
    private System.Windows.Forms.ComboBox cbxProductVersion;
    private System.Windows.Forms.ComboBox cbxProduct;
    private System.Windows.Forms.ComboBox cbxVendor;
    private System.Windows.Forms.Label label8;
    private System.Windows.Forms.Label label7;
    private System.Windows.Forms.Label label6;
  }
}

