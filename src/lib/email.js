import nodemailer from 'nodemailer';

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
});

export async function sendLeadAlert(data) {
  if (!process.env.EMAIL_USER) return; 

  const { contactName, companyName, email, phone, serviceType, ...details } = data;

  const detailsList = Object.entries(details)
    .map(([key, val]) => `<li style="margin-bottom: 5px;"><strong>${key}:</strong> ${val}</li>`)
    .join('');

  const mailOptions = {
    from: `"Elite Clean Bot" <${process.env.EMAIL_USER}>`,
    to: process.env.EMAIL_TO,
    subject: `💰 New Lead: ${serviceType.toUpperCase()} - ${contactName}`,
    html: `
      <div style="font-family: Arial, sans-serif; max-width: 600px; border: 1px solid #e0e0e0; padding: 20px; border-radius: 8px;">
        <h2 style="color: #003B2B; margin-top: 0;">New Quote Request</h2>
        <div style="background-color: #f9fafb; padding: 15px; border-radius: 6px; margin: 20px 0;">
          <h3 style="margin: 0 0 10px 0; color: #111;">Client Details</h3>
          <p style="margin: 5px 0;"><strong>Name:</strong> ${contactName}</p>
          <p style="margin: 5px 0;"><strong>Company:</strong> ${companyName || 'N/A'}</p>
          <p style="margin: 5px 0;"><strong>Phone:</strong> <a href="tel:${phone}">${phone}</a></p>
          <p style="margin: 5px 0;"><strong>Email:</strong> ${email}</p>
        </div>
        <div style="border-left: 4px solid #ff5e00; padding-left: 15px; margin: 20px 0;">
          <h3 style="margin: 0 0 10px 0; color: #111;">Scope: <span style="text-transform: capitalize;">${serviceType}</span></h3>
          <ul style="padding-left: 20px; color: #555;">${detailsList}</ul>
        </div>
        <a href="mailto:${email}" style="display: inline-block; background-color: #003B2B; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">Reply to Client</a>
      </div>
    `,
  };

  try {
    await transporter.sendMail(mailOptions);
    console.log('📧 Alert email sent successfully');
  } catch (error) {
    console.error('❌ Failed to send email alert:', error);
  }
}